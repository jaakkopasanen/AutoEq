# Audio Technica ATH-WS99

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 2.4; 25 1.9; 28 1.2; 31 0.7; 34 0.3; 37 -0.1; 41 -0.5; 45 -0.9; 49 -1.2; 54 -1.5; 60 -1.8; 66 -2.0; 72 -2.5; 79 -3.2; 87 -3.4; 96 -4.2; 106 -4.7; 116 -4.9; 128 -5.2; 141 -5.2; 155 -5.4; 170 -5.2; 187 -5.3; 206 -5.2; 227 -4.9; 249 -4.5; 274 -3.9; 302 -3.5; 332 -3.0; 365 -2.3; 402 -1.7; 442 -1.3; 486 -0.4; 535 0.8; 588 2.6; 647 3.5; 712 3.4; 783 2.9; 861 1.8; 947 0.7; 1042 -0.3; 1146 -1.1; 1261 -1.8; 1387 -2.5; 1526 -2.9; 1678 -2.7; 1846 -1.6; 2031 -0.1; 2234 1.6; 2457 3.7; 2703 5.6; 2973 6.0; 3270 6.0; 3597 6.0; 3957 6.0; 4353 2.3; 4788 -1.6; 5267 2.3; 5793 5.9; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audio Technica ATH-WS99 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audio Technica ATH-WS99 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.3dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 11 Hz   | 0.46 | 4.7 dB  |
| Peaking | 601 Hz  | 0.12 | -7.3 dB |
| Peaking | 670 Hz  | 0.98 | 10.4 dB |
| Peaking | 3110 Hz | 1.46 | 11.5 dB |
| Peaking | 6129 Hz | 4.36 | 7.1 dB  |
| Peaking | 1620 Hz | 3.85 | -1.4 dB |
| Peaking | 2592 Hz | 2.85 | 1.5 dB  |
| Peaking | 3214 Hz | 3.07 | -3.8 dB |
| Peaking | 4016 Hz | 1.9  | 4.2 dB  |
| Peaking | 4745 Hz | 6.13 | -6.5 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Audio%20Technica%20ATH-WS99/Audio%20Technica%20ATH-WS99.png)