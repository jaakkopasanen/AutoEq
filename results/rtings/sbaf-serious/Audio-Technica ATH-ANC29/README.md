# Audio-Technica ATH-ANC29

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 4.5; 25 4.8; 28 4.9; 31 4.9; 34 4.9; 37 4.8; 41 4.7; 45 4.5; 49 4.3; 54 4.2; 60 4.0; 66 3.9; 72 3.8; 79 3.8; 87 3.5; 96 3.3; 106 3.0; 116 2.7; 128 2.4; 141 2.1; 155 1.9; 170 1.8; 187 1.7; 206 1.6; 227 1.6; 249 1.7; 274 1.8; 302 1.8; 332 1.8; 365 1.8; 402 1.5; 442 1.3; 486 1.0; 535 0.7; 588 0.4; 647 0.3; 712 0.1; 783 -0.3; 861 1.2; 947 1.6; 1042 -1.5; 1146 -4.4; 1261 -3.6; 1387 -1.4; 1526 1.3; 1678 3.6; 1846 5.1; 2031 5.9; 2234 6.0; 2457 6.0; 2703 6.0; 2973 6.0; 3270 6.0; 3597 6.0; 3957 6.0; 4353 6.0; 4788 6.0; 5267 6.0; 5793 6.0; 6373 2.0; 7010 1.2; 7711 0.3; 8482 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audio-Technica ATH-ANC29 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audio-Technica ATH-ANC29 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 34 Hz   | 0.3  | 4.8 dB  |
| Peaking | 353 Hz  | 1.05 | 1.1 dB  |
| Peaking | 642 Hz  | 2.42 | -1.0 dB |
| Peaking | 1220 Hz | 3.6  | -7.8 dB |
| Peaking | 2877 Hz | 0.61 | 6.9 dB  |
| Peaking | 1972 Hz | 5.11 | 1.2 dB  |
| Peaking | 2876 Hz | 2.78 | -0.5 dB |
| Peaking | 4969 Hz | 2.14 | 4.0 dB  |
| Peaking | 5843 Hz | 5.99 | 4.0 dB  |
| Peaking | 6113 Hz | 1.05 | -3.8 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/sbaf-serious/Audio-Technica%20ATH-ANC29/Audio-Technica%20ATH-ANC29.png)