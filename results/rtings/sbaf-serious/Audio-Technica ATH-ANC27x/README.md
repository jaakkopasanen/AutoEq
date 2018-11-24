# Audio-Technica ATH-ANC27x

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 -15.1; 23 -15.4; 25 -15.4; 28 -15.1; 31 -14.4; 34 -13.4; 37 -12.5; 41 -12.1; 45 -12.1; 49 -11.7; 54 -10.9; 60 -10.2; 66 -9.6; 72 -9.0; 79 -8.5; 87 -8.0; 96 -7.6; 106 -7.5; 116 -7.5; 128 -7.3; 141 -7.0; 155 -6.7; 170 -6.3; 187 -5.9; 206 -5.6; 227 -5.3; 249 -4.9; 274 -4.4; 302 -3.9; 332 -3.3; 365 -2.7; 402 -2.2; 442 -1.7; 486 -1.2; 535 -0.8; 588 -0.3; 647 0.5; 712 1.5; 783 1.6; 861 0.8; 947 0.6; 1042 -0.3; 1146 -0.1; 1261 0.4; 1387 1.8; 1526 4.0; 1678 6.0; 1846 6.0; 2031 6.0; 2234 6.0; 2457 6.0; 2703 5.7; 2973 4.6; 3270 6.0; 3597 6.0; 3957 6.0; 4353 6.0; 4788 6.0; 5267 6.0; 5793 2.9; 6373 -3.8; 7010 -2.0; 7711 -2.2; 8482 -0.6; 9330 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audio-Technica ATH-ANC27x GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audio-Technica ATH-ANC27x ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 23 Hz   | 0.8  | -9.5 dB  |
| Peaking | 59 Hz   | 0.22 | -7.7 dB  |
| Peaking | 2063 Hz | 1.35 | 5.3 dB   |
| Peaking | 5357 Hz | 1.19 | 12.9 dB  |
| Peaking | 6490 Hz | 1.78 | -13.2 dB |
| Peaking | 92 Hz   | 3.6  | 0.7 dB   |
| Peaking | 237 Hz  | 1.48 | -0.6 dB  |
| Peaking | 754 Hz  | 2.01 | 2.5 dB   |
| Peaking | 1174 Hz | 1.67 | -2.3 dB  |
| Peaking | 1633 Hz | 5.48 | 2.3 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/sbaf-serious/Audio-Technica%20ATH-ANC27x/Audio-Technica%20ATH-ANC27x.png)