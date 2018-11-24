# Massdrop x Fostex TH-X00 sn1927

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -5.2dB
GraphicEQ: 21 -0.6; 23 -0.9; 25 -1.2; 28 -1.4; 31 -1.5; 34 -1.5; 37 -1.5; 41 -1.4; 45 -1.4; 49 -1.3; 54 -1.3; 60 -1.2; 66 -1.1; 72 -1.2; 79 -1.5; 87 -1.7; 96 -1.9; 106 -2.1; 116 -2.2; 128 -2.4; 141 -2.4; 155 -2.4; 170 -2.2; 187 -2.2; 206 -2.0; 227 -1.6; 249 -1.2; 274 -0.9; 302 -0.6; 332 -0.4; 365 -0.1; 402 0.2; 442 0.6; 486 0.6; 535 0.6; 588 0.8; 647 0.5; 712 -0.0; 783 0.9; 861 0.7; 947 0.1; 1042 -0.1; 1146 0.1; 1261 0.0; 1387 -0.4; 1526 -0.9; 1678 -1.0; 1846 -0.6; 2031 0.1; 2234 0.7; 2457 1.8; 2703 2.7; 2973 4.6; 3270 4.8; 3597 4.5; 3957 4.1; 4353 3.0; 4788 2.8; 5267 1.3; 5793 1.8; 6373 2.0; 7010 2.3; 7711 0.3; 8482 0.0; 9330 0.0; 10263 -0.4; 11289 0.0; 12418 0.0; 13660 -0.3; 15026 -0.1
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Massdrop x Fostex TH-X00 sn1927 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-51**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Massdrop x Fostex TH-X00 sn1927 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.1dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 37 Hz   | 0.54 | -1.3 dB |
| Peaking | 149 Hz  | 1.16 | -2.4 dB |
| Peaking | 1762 Hz | 2.62 | -1.8 dB |
| Peaking | 3395 Hz | 1.6  | 5.1 dB  |
| Peaking | 6662 Hz | 5.79 | 1.8 dB  |
| Peaking | 228 Hz  | 3.11 | -0.5 dB |
| Peaking | 532 Hz  | 1.36 | 0.9 dB  |
| Peaking | 9615 Hz | 2.31 | -0.5 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Massdrop%20x%20Fostex%20TH-X00%20sn1927/Massdrop%20x%20Fostex%20TH-X00%20sn1927.png)