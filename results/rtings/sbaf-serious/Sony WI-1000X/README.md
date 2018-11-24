# Sony WI-1000X

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -3.1dB
GraphicEQ: 21 0.0; 23 1.4; 25 0.8; 28 0.4; 31 0.4; 34 0.6; 37 0.8; 41 1.0; 45 1.0; 49 0.9; 54 0.6; 60 0.2; 66 -0.3; 72 -0.6; 79 -0.9; 87 -1.4; 96 -2.0; 106 -2.6; 116 -3.2; 128 -3.7; 141 -4.1; 155 -4.3; 170 -4.5; 187 -4.6; 206 -4.8; 227 -4.8; 249 -4.8; 274 -4.7; 302 -4.7; 332 -4.5; 365 -4.1; 402 -3.6; 442 -2.9; 486 -2.6; 535 -2.8; 588 -3.2; 647 -2.2; 712 -1.3; 783 -1.0; 861 -0.9; 947 -0.8; 1042 0.6; 1146 0.1; 1261 -0.1; 1387 -0.3; 1526 -0.2; 1678 -0.6; 1846 -1.1; 2031 -1.9; 2234 -2.3; 2457 -1.7; 2703 -0.3; 2973 0.4; 3270 -0.3; 3597 -1.2; 3957 -2.5; 4353 -2.4; 4788 -2.4; 5267 -3.0; 5793 -1.6; 6373 0.6; 7010 1.3; 7711 0.3; 8482 -1.3; 9330 -5.9; 10263 -9.4; 11289 -7.0; 12418 -1.1; 13660 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sony WI-1000X GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-31**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony WI-1000X ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-1.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-1.4dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 21 Hz    | 0.1  | 1.4 dB   |
| Peaking | 144 Hz   | 0.83 | -3.8 dB  |
| Peaking | 313 Hz   | 0.77 | -3.8 dB  |
| Peaking | 2205 Hz  | 3.64 | -2.2 dB  |
| Peaking | 10403 Hz | 3.92 | -10.5 dB |
| Peaking | 590 Hz   | 8.94 | -1.3 dB  |
| Peaking | 3410 Hz  | 0.79 | 3.1 dB   |
| Peaking | 5383 Hz  | 0.82 | -7.1 dB  |
| Peaking | 6909 Hz  | 2    | 6.7 dB   |
| Peaking | 13362 Hz | 3.38 | 1.9 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/sbaf-serious/Sony%20WI-1000X/Sony%20WI-1000X.png)