# Sony MDR-7520

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 0.2; 25 -0.4; 28 -1.2; 31 -1.9; 34 -2.5; 37 -3.0; 41 -3.5; 45 -3.9; 49 -4.3; 54 -4.6; 60 -5.0; 66 -5.4; 72 -5.7; 79 -6.0; 87 -6.3; 96 -6.6; 106 -6.8; 116 -6.9; 128 -6.9; 141 -6.6; 155 -5.9; 170 -5.2; 187 -4.5; 206 -3.5; 227 -2.0; 249 -0.5; 274 -1.3; 302 1.2; 332 2.1; 365 1.7; 402 0.6; 442 -0.2; 486 -0.6; 535 -0.6; 588 -0.6; 647 -0.2; 712 -0.2; 783 -0.3; 861 -0.2; 947 -0.0; 1042 -0.0; 1146 -0.2; 1261 -0.8; 1387 -1.8; 1526 -3.0; 1678 -4.1; 1846 -5.0; 2031 -5.4; 2234 -5.0; 2457 -5.1; 2703 -6.0; 2973 -6.0; 3270 -3.2; 3597 0.5; 3957 4.4; 4353 6.0; 4788 6.0; 5267 3.7; 5793 2.5; 6373 5.2; 7010 2.5; 7711 -2.0; 8482 -9.7; 9330 -13.1; 10263 -8.3; 11289 -0.3; 12418 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sony MDR-7520 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony MDR-7520 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.6dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 99 Hz   | 0.73 | -7.3 dB  |
| Peaking | 1993 Hz | 0.9  | -13.7 dB |
| Peaking | 2987 Hz | 2.37 | -11.2 dB |
| Peaking | 3402 Hz | 0.4  | 14.0 dB  |
| Peaking | 9178 Hz | 2.83 | -20.0 dB |
| Peaking | 41 Hz   | 0.93 | -5.0 dB  |
| Peaking | 48 Hz   | 0.36 | 4.3 dB   |
| Peaking | 255 Hz  | 0.4  | -3.6 dB  |
| Peaking | 325 Hz  | 1.61 | 5.7 dB   |
| Peaking | 1139 Hz | 1.7  | 0.9 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/sbaf-serious/Sony%20MDR-7520/Sony%20MDR-7520.png)