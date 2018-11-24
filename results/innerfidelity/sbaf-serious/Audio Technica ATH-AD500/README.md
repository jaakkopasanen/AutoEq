# Audio Technica ATH-AD500

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 6.0; 41 6.0; 45 6.0; 49 6.0; 54 6.0; 60 6.0; 66 5.9; 72 5.3; 79 4.8; 87 3.9; 96 2.8; 106 2.2; 116 2.0; 128 1.4; 141 1.1; 155 1.0; 170 1.0; 187 0.9; 206 0.9; 227 1.1; 249 1.0; 274 1.0; 302 1.1; 332 1.1; 365 1.1; 402 1.3; 442 1.4; 486 1.2; 535 1.1; 588 1.3; 647 1.2; 712 1.1; 783 1.2; 861 0.7; 947 0.2; 1042 -0.2; 1146 -0.5; 1261 -1.0; 1387 -1.2; 1526 -1.0; 1678 -0.4; 1846 0.0; 2031 1.1; 2234 1.7; 2457 3.5; 2703 4.5; 2973 6.0; 3270 6.0; 3597 6.0; 3957 2.9; 4353 1.4; 4788 2.3; 5267 5.5; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 -0.9; 9330 -3.0; 10263 -0.7; 11289 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audio Technica ATH-AD500 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audio Technica ATH-AD500 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 37 Hz   | 0.5  | 6.7 dB  |
| Peaking | 486 Hz  | 1.52 | 1.3 dB  |
| Peaking | 3137 Hz | 2.66 | 6.5 dB  |
| Peaking | 5922 Hz | 3.15 | 6.3 dB  |
| Peaking | 9191 Hz | 4.17 | -3.5 dB |
| Peaking | 70 Hz   | 1.69 | 3.3 dB  |
| Peaking | 73 Hz   | 0.82 | -2.2 dB |
| Peaking | 1436 Hz | 1.41 | -3.3 dB |
| Peaking | 1538 Hz | 0.56 | 1.7 dB  |
| Peaking | 4306 Hz | 8.93 | -2.1 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Audio%20Technica%20ATH-AD500/Audio%20Technica%20ATH-AD500.png)