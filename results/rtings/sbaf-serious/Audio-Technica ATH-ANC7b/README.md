# Audio-Technica ATH-ANC7b

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.4dB
GraphicEQ: 21 0.0; 23 5.4; 25 4.9; 28 4.1; 31 3.5; 34 2.9; 37 2.4; 41 1.9; 45 1.5; 49 1.2; 54 0.8; 60 0.5; 66 0.2; 72 0.0; 79 -0.1; 87 -0.4; 96 -0.7; 106 -1.0; 116 -1.3; 128 -1.5; 141 -1.6; 155 -1.6; 170 -1.6; 187 -1.4; 206 -1.2; 227 -1.0; 249 -0.7; 274 -0.5; 302 -0.3; 332 -0.1; 365 0.0; 402 -0.0; 442 0.0; 486 0.2; 535 0.7; 588 1.2; 647 1.8; 712 1.9; 783 0.6; 861 -1.0; 947 -0.9; 1042 2.1; 1146 5.4; 1261 5.0; 1387 5.0; 1526 5.6; 1678 5.4; 1846 6.0; 2031 6.0; 2234 6.0; 2457 6.0; 2703 6.0; 2973 6.0; 3270 6.0; 3597 6.0; 3957 6.0; 4353 6.0; 4788 6.0; 5267 6.0; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audio-Technica ATH-ANC7b GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-63**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audio-Technica ATH-ANC7b ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 18 Hz   | 0.7  | 6.6 dB  |
| Peaking | 188 Hz  | 0.56 | -2.2 dB |
| Peaking | 296 Hz  | 1.19 | 1.1 dB  |
| Peaking | 2123 Hz | 0.75 | 6.2 dB  |
| Peaking | 5102 Hz | 1.78 | 4.8 dB  |
| Peaking | 685 Hz  | 3.49 | 2.1 dB  |
| Peaking | 951 Hz  | 2.8  | -5.6 dB |
| Peaking | 1117 Hz | 3.47 | 4.8 dB  |
| Peaking | 6401 Hz | 4.91 | 3.1 dB  |
| Peaking | 7706 Hz | 1.81 | -2.2 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/sbaf-serious/Audio-Technica%20ATH-ANC7b/Audio-Technica%20ATH-ANC7b.png)