# Audio-Technica ATH-M20x

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 5.9; 25 5.5; 28 4.5; 31 3.4; 34 2.4; 37 1.6; 41 0.7; 45 -0.1; 49 -0.8; 54 -1.5; 60 -2.2; 66 -2.5; 72 -2.6; 79 -2.4; 87 -2.2; 96 -2.1; 106 -2.2; 116 -2.3; 128 -2.3; 141 -1.7; 155 -0.9; 170 0.2; 187 1.4; 206 2.8; 227 4.0; 249 4.4; 274 3.4; 302 2.2; 332 1.6; 365 1.2; 402 0.7; 442 0.3; 486 0.2; 535 0.1; 588 0.1; 647 0.1; 712 0.2; 783 0.2; 861 0.1; 947 -0.0; 1042 0.2; 1146 0.2; 1261 -0.2; 1387 -1.1; 1526 -2.1; 1678 -2.8; 1846 -3.3; 2031 -3.4; 2234 -2.8; 2457 -1.4; 2703 0.1; 2973 1.3; 3270 3.1; 3597 5.8; 3957 6.0; 4353 4.8; 4788 5.9; 5267 6.0; 5793 6.0; 6373 5.5; 7010 2.5; 7711 -0.0; 8482 -1.4; 9330 -0.2; 10263 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audio-Technica ATH-M20x GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audio-Technica ATH-M20x ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 22 Hz   | 0.89 | 7.3 dB  |
| Peaking | 76 Hz   | 0.42 | -3.7 dB |
| Peaking | 239 Hz  | 1.77 | 5.8 dB  |
| Peaking | 2017 Hz | 1.99 | -4.8 dB |
| Peaking | 4519 Hz | 1.3  | 6.9 dB  |
| Peaking | 1107 Hz | 5.08 | 0.8 dB  |
| Peaking | 3706 Hz | 4.9  | 3.6 dB  |
| Peaking | 4158 Hz | 2.05 | -2.8 dB |
| Peaking | 6285 Hz | 2.47 | 3.9 dB  |
| Peaking | 8025 Hz | 2.46 | -3.7 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/sbaf-serious/Audio-Technica%20ATH-M20x/Audio-Technica%20ATH-M20x.png)