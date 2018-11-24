# Audio-Technica ATH-ANC27x

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 -15.5; 23 -15.7; 25 -15.7; 28 -15.2; 31 -14.4; 34 -13.4; 37 -12.4; 41 -11.9; 45 -11.8; 49 -11.3; 54 -10.6; 60 -9.9; 66 -9.5; 72 -9.0; 79 -8.7; 87 -8.3; 96 -8.0; 106 -8.0; 116 -8.0; 128 -7.8; 141 -7.5; 155 -7.3; 170 -6.9; 187 -6.5; 206 -6.1; 227 -5.8; 249 -5.4; 274 -5.1; 302 -4.7; 332 -4.2; 365 -3.7; 402 -3.3; 442 -2.8; 486 -2.4; 535 -2.0; 588 -1.4; 647 -0.6; 712 0.6; 783 1.1; 861 0.6; 947 0.5; 1042 -0.4; 1146 -0.3; 1261 0.1; 1387 1.8; 1526 4.4; 1678 6.0; 1846 6.0; 2031 6.0; 2234 6.0; 2457 6.0; 2703 5.1; 2973 3.5; 3270 5.5; 3597 6.0; 3957 6.0; 4353 6.0; 4788 6.0; 5267 5.9; 5793 1.4; 6373 -6.3; 7010 -4.5; 7711 -3.3; 8482 -0.8; 9330 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audio-Technica ATH-ANC27x GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audio-Technica ATH-ANC27x ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 21 Hz   | 0.38 | -15.4 dB |
| Peaking | 179 Hz  | 0.51 | -5.0 dB  |
| Peaking | 1967 Hz | 1.7  | 5.5 dB   |
| Peaking | 5337 Hz | 1.16 | 13.8 dB  |
| Peaking | 6503 Hz | 2.09 | -17.0 dB |
| Peaking | 788 Hz  | 3.32 | 2.2 dB   |
| Peaking | 1292 Hz | 1.52 | -2.2 dB  |
| Peaking | 1577 Hz | 4.68 | 2.9 dB   |
| Peaking | 3567 Hz | 6.93 | 1.2 dB   |
| Peaking | 4665 Hz | 7.36 | -0.7 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/rtings/Audio-Technica%20ATH-ANC27x/Audio-Technica%20ATH-ANC27x.png)