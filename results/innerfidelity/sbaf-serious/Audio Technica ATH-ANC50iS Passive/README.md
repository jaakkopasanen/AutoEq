# Audio Technica ATH-ANC50iS Passive

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 -0.9; 23 -1.7; 25 -2.4; 28 -3.2; 31 -3.9; 34 -4.5; 37 -4.8; 41 -5.2; 45 -5.5; 49 -5.8; 54 -6.0; 60 -6.1; 66 -6.2; 72 -6.2; 79 -6.2; 87 -6.8; 96 -7.3; 106 -7.6; 116 -7.6; 128 -7.9; 141 -8.2; 155 -8.4; 170 -8.4; 187 -8.8; 206 -8.9; 227 -8.9; 249 -8.8; 274 -8.6; 302 -7.7; 332 -7.1; 365 -7.1; 402 -6.9; 442 -7.0; 486 -6.6; 535 -4.9; 588 -2.4; 647 -0.2; 712 1.0; 783 1.9; 861 0.9; 947 -0.3; 1042 0.9; 1146 2.6; 1261 4.1; 1387 5.3; 1526 6.0; 1678 6.0; 1846 6.0; 2031 6.0; 2234 6.0; 2457 6.0; 2703 6.0; 2973 6.0; 3270 6.0; 3597 6.0; 3957 6.0; 4353 6.0; 4788 6.0; 5267 6.0; 5793 6.0; 6373 5.4; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audio Technica ATH-ANC50iS Passive GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audio Technica ATH-ANC50iS Passive ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 85 Hz   | 0.36 | -6.1 dB |
| Peaking | 248 Hz  | 0.89 | -5.7 dB |
| Peaking | 462 Hz  | 3.11 | -4.3 dB |
| Peaking | 2086 Hz | 0.66 | 6.4 dB  |
| Peaking | 5160 Hz | 1.92 | 4.5 dB  |
| Peaking | 781 Hz  | 3.31 | 3.6 dB  |
| Peaking | 940 Hz  | 2.75 | -3.6 dB |
| Peaking | 1402 Hz | 3.99 | 1.4 dB  |
| Peaking | 6419 Hz | 4.96 | 3.0 dB  |
| Peaking | 7764 Hz | 1.81 | -2.2 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Audio%20Technica%20ATH-ANC50iS%20Passive/Audio%20Technica%20ATH-ANC50iS%20Passive.png)