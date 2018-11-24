# Audio Technica ATH-A1000X

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 5.5; 25 4.9; 28 4.0; 31 3.1; 34 2.3; 37 1.7; 41 1.0; 45 0.4; 49 -0.1; 54 -0.5; 60 -0.8; 66 -0.9; 72 -0.6; 79 -0.2; 87 -0.2; 96 0.0; 106 -0.5; 116 -1.6; 128 -2.2; 141 -2.1; 155 -1.2; 170 -0.3; 187 -1.0; 206 -0.5; 227 0.3; 249 0.9; 274 1.2; 302 1.1; 332 1.2; 365 1.1; 402 0.9; 442 0.8; 486 0.6; 535 0.4; 588 0.6; 647 0.6; 712 0.3; 783 0.4; 861 0.3; 947 0.0; 1042 -0.0; 1146 -0.3; 1261 0.1; 1387 -0.5; 1526 -0.4; 1678 -0.1; 1846 -1.6; 2031 -4.2; 2234 -1.8; 2457 1.0; 2703 3.6; 2973 6.0; 3270 6.0; 3597 6.0; 3957 6.0; 4353 4.2; 4788 5.3; 5267 6.0; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0; 9330 0.0; 10263 0.0; 11289 0.0; 12418 0.0; 13660 0.0; 15026 0.0; 16529 -0.3; 18182 -2.9; 20000 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audio Technica ATH-A1000X GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audio Technica ATH-A1000X ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 22 Hz    | 1.86 | 6.2 dB  |
| Peaking | 132 Hz   | 3.45 | -2.5 dB |
| Peaking | 2073 Hz  | 3.88 | -6.2 dB |
| Peaking | 3296 Hz  | 1.56 | 6.6 dB  |
| Peaking | 5733 Hz  | 3.14 | 5.3 dB  |
| Peaking | 32 Hz    | 2.1  | 0.8 dB  |
| Peaking | 58 Hz    | 2.44 | -1.2 dB |
| Peaking | 336 Hz   | 1.67 | 1.3 dB  |
| Peaking | 8246 Hz  | 4.57 | -1.2 dB |
| Peaking | 18495 Hz | 2.83 | -3.2 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Audio%20Technica%20ATH-A1000X/Audio%20Technica%20ATH-A1000X.png)