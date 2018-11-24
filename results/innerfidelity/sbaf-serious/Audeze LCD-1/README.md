# Audeze LCD-1

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 5.9; 41 5.6; 45 5.2; 49 4.9; 54 4.6; 60 4.4; 66 4.4; 72 4.2; 79 3.9; 87 2.9; 96 2.4; 106 2.0; 116 1.9; 128 1.6; 141 1.4; 155 1.2; 170 1.2; 187 1.0; 206 0.8; 227 0.8; 249 0.9; 274 1.0; 302 1.1; 332 1.3; 365 1.1; 402 0.9; 442 0.8; 486 0.6; 535 0.6; 588 0.9; 647 0.8; 712 0.5; 783 0.8; 861 0.9; 947 0.3; 1042 -0.2; 1146 -0.8; 1261 -1.3; 1387 -1.3; 1526 -1.7; 1678 -2.4; 1846 -2.1; 2031 -2.3; 2234 -2.4; 2457 -1.6; 2703 -1.8; 2973 -1.4; 3270 -1.7; 3597 -2.2; 3957 -3.6; 4353 -5.9; 4788 -6.2; 5267 -4.3; 5793 -3.0; 6373 -0.5; 7010 1.0; 7711 0.1; 8482 -3.2; 9330 -4.1; 10263 -3.2; 11289 -1.4; 12418 0.0; 13660 0.0; 15026 0.0; 16529 0.0; 18182 -0.7; 20000 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audeze LCD-1 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audeze LCD-1 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.3dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 29 Hz    | 0.4  | 6.2 dB  |
| Peaking | 780 Hz   | 0.51 | 1.2 dB  |
| Peaking | 1725 Hz  | 1.04 | -2.8 dB |
| Peaking | 4667 Hz  | 2.67 | -6.2 dB |
| Peaking | 21590 Hz | 1.69 | -2.6 dB |
| Peaking | 74 Hz    | 3.06 | 1.4 dB  |
| Peaking | 78 Hz    | 1.3  | -0.8 dB |
| Peaking | 7197 Hz  | 4.77 | 3.4 dB  |
| Peaking | 9265 Hz  | 2.91 | -4.5 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Audeze%20LCD-1/Audeze%20LCD-1.png)