# Audio Technica ATH-AD2000X

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 6.0; 41 6.0; 45 6.0; 49 6.0; 54 6.0; 60 6.0; 66 5.8; 72 5.4; 79 4.9; 87 4.5; 96 4.0; 106 3.4; 116 2.9; 128 2.5; 141 2.1; 155 1.8; 170 1.7; 187 1.3; 206 1.2; 227 1.1; 249 1.0; 274 1.0; 302 0.9; 332 0.9; 365 0.9; 402 0.9; 442 1.0; 486 0.7; 535 0.7; 588 0.9; 647 0.7; 712 0.8; 783 0.6; 861 0.4; 947 0.2; 1042 0.1; 1146 0.2; 1261 0.5; 1387 0.4; 1526 0.8; 1678 1.4; 1846 3.1; 2031 4.7; 2234 6.0; 2457 6.0; 2703 6.0; 2973 6.0; 3270 6.0; 3597 4.1; 3957 2.5; 4353 4.3; 4788 6.0; 5267 6.0; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audio Technica ATH-AD2000X GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audio Technica ATH-AD2000X ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 23 Hz    | 0.28 | 5.8 dB  |
| Peaking | 68 Hz    | 1.05 | 1.9 dB  |
| Peaking | 427 Hz   | 1.55 | 0.6 dB  |
| Peaking | 2628 Hz  | 1.65 | 6.4 dB  |
| Peaking | 5483 Hz  | 2.46 | 6.0 dB  |
| Peaking | 1494 Hz  | 1.88 | -0.9 dB |
| Peaking | 2060 Hz  | 5.86 | 1.6 dB  |
| Peaking | 6583 Hz  | 6.78 | 2.4 dB  |
| Peaking | 7626 Hz  | 2.67 | -1.5 dB |
| Peaking | 10397 Hz | 1.52 | -0.3 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Audio%20Technica%20ATH-AD2000X/Audio%20Technica%20ATH-AD2000X.png)