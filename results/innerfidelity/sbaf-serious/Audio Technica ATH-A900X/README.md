# Audio Technica ATH-A900X

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.4dB
GraphicEQ: 21 0.0; 23 5.2; 25 4.6; 28 3.7; 31 2.9; 34 2.2; 37 1.7; 41 1.1; 45 0.6; 49 0.2; 54 -0.1; 60 -0.8; 66 -1.4; 72 -1.5; 79 -1.6; 87 -2.6; 96 -3.0; 106 -3.2; 116 -3.6; 128 -4.3; 141 -4.6; 155 -4.3; 170 -3.9; 187 -4.3; 206 -4.0; 227 -3.3; 249 -2.7; 274 -1.7; 302 -1.0; 332 -0.7; 365 -0.9; 402 -1.0; 442 -1.0; 486 -1.2; 535 -1.3; 588 -1.0; 647 -0.5; 712 0.2; 783 0.2; 861 -0.1; 947 -0.1; 1042 0.1; 1146 0.2; 1261 0.8; 1387 1.4; 1526 1.2; 1678 0.8; 1846 -0.7; 2031 -1.3; 2234 -0.4; 2457 1.8; 2703 3.5; 2973 4.7; 3270 4.8; 3597 5.6; 3957 5.9; 4353 3.1; 4788 5.8; 5267 6.0; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0; 9330 0.0; 10263 0.0; 11289 0.0; 12418 0.0; 13660 0.0; 15026 0.0; 16529 -0.2; 18182 -0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audio Technica ATH-A900X GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-64**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audio Technica ATH-A900X ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 20 Hz   | 1.01 | 6.2 dB  |
| Peaking | 136 Hz  | 0.81 | -4.2 dB |
| Peaking | 203 Hz  | 3.03 | -1.2 dB |
| Peaking | 3483 Hz | 2.22 | 5.3 dB  |
| Peaking | 5641 Hz | 2.77 | 5.9 dB  |
| Peaking | 530 Hz  | 4.75 | -1.0 dB |
| Peaking | 1526 Hz | 2.58 | 2.0 dB  |
| Peaking | 2028 Hz | 2.66 | -3.0 dB |
| Peaking | 2660 Hz | 4.56 | 1.9 dB  |
| Peaking | 8283 Hz | 4.53 | -1.2 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Audio%20Technica%20ATH-A900X/Audio%20Technica%20ATH-A900X.png)