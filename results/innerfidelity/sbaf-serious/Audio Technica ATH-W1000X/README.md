# Audio Technica ATH-W1000X

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 6.0; 41 5.7; 45 4.8; 49 3.9; 54 2.9; 60 1.5; 66 0.6; 72 -0.0; 79 -1.0; 87 -1.7; 96 -2.1; 106 -2.4; 116 -2.3; 128 -2.4; 141 -2.4; 155 -2.3; 170 -1.9; 187 -1.8; 206 -1.7; 227 -1.3; 249 -1.0; 274 -0.5; 302 -0.1; 332 0.4; 365 1.0; 402 2.0; 442 3.1; 486 2.6; 535 1.4; 588 0.6; 647 0.4; 712 0.2; 783 1.1; 861 0.7; 947 -0.0; 1042 0.0; 1146 0.1; 1261 -0.3; 1387 -0.7; 1526 -1.5; 1678 -1.3; 1846 -0.8; 2031 -0.9; 2234 -0.5; 2457 1.0; 2703 3.6; 2973 5.0; 3270 5.8; 3597 5.7; 3957 5.7; 4353 3.4; 4788 5.8; 5267 6.0; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0; 9330 0.0; 10263 0.0; 11289 0.0; 12418 0.0; 13660 0.0; 15026 0.0; 16529 -0.2; 18182 -2.4; 20000 -1.7
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audio Technica ATH-W1000X GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audio Technica ATH-W1000X ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 35 Hz    | 0.49 | 8.5 dB  |
| Peaking | 91 Hz    | 0.57 | -5.9 dB |
| Peaking | 449 Hz   | 2.76 | 3.5 dB  |
| Peaking | 3401 Hz  | 2.85 | 5.8 dB  |
| Peaking | 5557 Hz  | 2.57 | 6.2 dB  |
| Peaking | 809 Hz   | 8.27 | 1.3 dB  |
| Peaking | 1852 Hz  | 1.67 | -1.8 dB |
| Peaking | 2777 Hz  | 6.23 | 2.1 dB  |
| Peaking | 8200 Hz  | 5.47 | -1.2 dB |
| Peaking | 18819 Hz | 1.98 | -2.8 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Audio%20Technica%20ATH-W1000X/Audio%20Technica%20ATH-W1000X.png)