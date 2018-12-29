# Audio Technica ATH-ANC7b
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 5.8; 31 5.4; 34 4.9; 37 4.5; 41 4.0; 45 3.7; 49 3.4; 54 3.0; 60 2.6; 66 2.3; 72 2.0; 79 1.7; 87 1.4; 96 1.0; 106 1.0; 116 0.9; 128 0.9; 141 0.7; 155 0.7; 170 0.9; 187 1.1; 206 1.2; 227 1.5; 249 1.8; 274 2.1; 302 2.4; 332 2.7; 365 2.8; 402 3.0; 442 2.9; 486 2.6; 535 2.7; 588 2.8; 647 2.8; 712 2.0; 783 0.4; 861 -0.1; 947 -0.1; 1042 -0.3; 1146 0.7; 1261 4.9; 1387 5.9; 1526 5.5; 1678 6.0; 1846 6.0; 2031 5.4; 2234 6.0; 2457 6.0; 2703 6.0; 2973 6.0; 3270 6.0; 3597 6.0; 3957 6.0; 4353 6.0; 4788 6.0; 5267 6.0; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audio Technica ATH-ANC7b GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audio Technica ATH-ANC7b ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 24 Hz   | 0.8  | 6.0 dB  |
| Peaking | 54 Hz   | 1.29 | 1.1 dB  |
| Peaking | 388 Hz  | 0.93 | 2.1 dB  |
| Peaking | 961 Hz  | 2.5  | -5.2 dB |
| Peaking | 2394 Hz | 0.41 | 6.8 dB  |
| Peaking | 1147 Hz | 7.18 | -3.2 dB |
| Peaking | 1273 Hz | 3.35 | 2.7 dB  |
| Peaking | 2240 Hz | 1.43 | -0.9 dB |
| Peaking | 6202 Hz | 1.67 | 7.0 dB  |
| Peaking | 7446 Hz | 1.33 | -6.2 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Audio%20Technica%20ATH-ANC7b/Audio%20Technica%20ATH-ANC7b.png)