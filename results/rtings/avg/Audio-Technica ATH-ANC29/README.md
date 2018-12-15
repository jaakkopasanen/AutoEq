# Audio-Technica ATH-ANC29

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.3dB
GraphicEQ: 21 0.0; 23 4.2; 25 4.5; 28 4.8; 31 4.8; 34 4.9; 37 4.9; 41 4.9; 45 4.8; 49 4.7; 54 4.5; 60 4.3; 66 4.1; 72 3.8; 79 3.6; 87 3.2; 96 2.9; 106 2.5; 116 2.2; 128 1.9; 141 1.6; 155 1.3; 170 1.2; 187 1.1; 206 1.1; 227 1.1; 249 1.2; 274 1.1; 302 1.0; 332 0.8; 365 0.8; 402 0.5; 442 0.1; 486 -0.2; 535 -0.5; 588 -0.7; 647 -0.7; 712 -0.8; 783 -0.7; 861 1.0; 947 1.6; 1042 -1.5; 1146 -4.6; 1261 -3.9; 1387 -1.4; 1526 1.7; 1678 3.9; 1846 5.0; 2031 5.5; 2234 6.0; 2457 6.0; 2703 5.3; 2973 5.2; 3270 6.0; 3597 6.0; 3957 6.0; 4353 6.0; 4788 6.0; 5267 6.1; 5793 5.0; 6373 -1.8; 7010 -2.2; 7711 -0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audio-Technica ATH-ANC29 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-62**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audio-Technica ATH-ANC29 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 40 Hz   | 0.45 | 5.4 dB  |
| Peaking | 44 Hz   | 1.47 | -0.6 dB |
| Peaking | 1209 Hz | 3.95 | -7.7 dB |
| Peaking | 3225 Hz | 0.59 | 6.9 dB  |
| Peaking | 6856 Hz | 5.08 | -6.7 dB |
| Peaking | 633 Hz  | 3.11 | -1.6 dB |
| Peaking | 1972 Hz | 2.88 | 1.3 dB  |
| Peaking | 2924 Hz | 4.05 | -1.6 dB |
| Peaking | 5467 Hz | 5.25 | 2.9 dB  |
| Peaking | 9910 Hz | 1.19 | -1.3 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Audio-Technica%20ATH-ANC29/Audio-Technica%20ATH-ANC29.png)