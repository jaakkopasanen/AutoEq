# Sony WI-1000X

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -2.7dB
GraphicEQ: 21 0.0; 23 1.1; 25 0.5; 28 0.2; 31 0.4; 34 0.7; 37 0.9; 41 1.2; 45 1.2; 49 1.2; 54 1.0; 60 0.4; 66 -0.1; 72 -0.6; 79 -1.1; 87 -1.7; 96 -2.4; 106 -3.1; 116 -3.7; 128 -4.3; 141 -4.7; 155 -4.9; 170 -5.1; 187 -5.2; 206 -5.3; 227 -5.3; 249 -5.3; 274 -5.4; 302 -5.5; 332 -5.4; 365 -5.2; 402 -4.6; 442 -4.0; 486 -3.8; 535 -4.0; 588 -4.3; 647 -3.3; 712 -2.2; 783 -1.5; 861 -1.1; 947 -0.9; 1042 0.6; 1146 -0.1; 1261 -0.4; 1387 -0.2; 1526 0.2; 1678 -0.3; 1846 -1.1; 2031 -2.3; 2234 -2.8; 2457 -2.1; 2703 -0.9; 2973 -0.7; 3270 -2.1; 3597 -3.4; 3957 -3.7; 4353 -2.4; 4788 -2.2; 5267 -3.4; 5793 -3.0; 6373 -2.0; 7010 -1.3; 7711 -0.5; 8482 -1.6; 9330 -7.4; 10263 -12.8; 11289 -11.5; 12418 -5.6; 13660 -1.1; 15026 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sony WI-1000X GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-26**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony WI-1000X ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-2.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-0.0dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 148 Hz   | 1.4  | -3.3 dB  |
| Peaking | 331 Hz   | 0.75 | -5.1 dB  |
| Peaking | 3755 Hz  | 2.38 | -3.1 dB  |
| Peaking | 5477 Hz  | 4.78 | -2.2 dB  |
| Peaking | 10674 Hz | 3.43 | -14.5 dB |
| Peaking | 17 Hz    | 2.35 | 3.4 dB   |
| Peaking | 48 Hz    | 2.4  | 1.7 dB   |
| Peaking | 1073 Hz  | 4.47 | 1.5 dB   |
| Peaking | 2221 Hz  | 4.72 | -2.4 dB  |
| Peaking | 2929 Hz  | 7.02 | 1.3 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/rtings/Sony%20WI-1000X/Sony%20WI-1000X.png)