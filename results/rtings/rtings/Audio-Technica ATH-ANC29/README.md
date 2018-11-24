# Audio-Technica ATH-ANC29

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 4.2; 25 4.5; 28 4.8; 31 4.8; 34 4.9; 37 4.9; 41 4.9; 45 4.8; 49 4.7; 54 4.5; 60 4.3; 66 4.1; 72 3.8; 79 3.6; 87 3.2; 96 2.9; 106 2.5; 116 2.2; 128 1.9; 141 1.6; 155 1.3; 170 1.2; 187 1.1; 206 1.1; 227 1.1; 249 1.2; 274 1.1; 302 1.0; 332 0.8; 365 0.8; 402 0.5; 442 0.1; 486 -0.2; 535 -0.5; 588 -0.7; 647 -0.7; 712 -0.8; 783 -0.7; 861 1.0; 947 1.6; 1042 -1.5; 1146 -4.6; 1261 -3.9; 1387 -1.4; 1526 1.7; 1678 3.9; 1846 5.0; 2031 5.5; 2234 6.0; 2457 6.0; 2703 5.5; 2973 5.7; 3270 6.0; 3597 6.0; 3957 6.0; 4353 6.0; 4788 6.0; 5267 6.0; 5793 6.0; 6373 -0.6; 7010 -1.4; 7711 0.3; 8482 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audio-Technica ATH-ANC29 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audio-Technica ATH-ANC29 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 38 Hz   | 0.4  | 4.8 dB  |
| Peaking | 42 Hz   | 0.64 | 0.1 dB  |
| Peaking | 1222 Hz | 3.94 | -7.3 dB |
| Peaking | 2338 Hz | 1.03 | 6.3 dB  |
| Peaking | 4702 Hz | 2.37 | 5.0 dB  |
| Peaking | 717 Hz  | 2.02 | -1.5 dB |
| Peaking | 914 Hz  | 7.73 | 2.9 dB  |
| Peaking | 3509 Hz | 6.66 | 1.2 dB  |
| Peaking | 5892 Hz | 6.38 | 5.6 dB  |
| Peaking | 6523 Hz | 4.35 | -5.7 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/rtings/Audio-Technica%20ATH-ANC29/Audio-Technica%20ATH-ANC29.png)