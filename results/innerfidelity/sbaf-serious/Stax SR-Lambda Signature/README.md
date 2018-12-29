# Stax SR-Lambda Signature
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 5.6; 34 4.2; 37 2.4; 41 0.4; 45 -1.0; 49 -1.7; 54 -1.6; 60 -1.2; 66 -0.3; 72 0.4; 79 0.5; 87 0.6; 96 0.7; 106 0.9; 116 1.1; 128 1.1; 141 1.2; 155 1.2; 170 1.2; 187 1.3; 206 1.3; 227 1.4; 249 1.4; 274 1.5; 302 1.5; 332 1.5; 365 1.4; 402 1.5; 442 1.8; 486 1.8; 535 1.6; 588 1.7; 647 1.5; 712 1.2; 783 1.2; 861 0.8; 947 0.4; 1042 -0.2; 1146 -0.6; 1261 -1.6; 1387 -2.9; 1526 -3.8; 1678 -4.2; 1846 -4.3; 2031 -2.1; 2234 1.0; 2457 4.0; 2703 2.6; 2973 1.4; 3270 0.8; 3597 0.6; 3957 0.0; 4353 -0.6; 4788 0.3; 5267 1.9; 5793 2.7; 6373 0.3; 7010 -0.8; 7711 -0.0; 8482 -2.5; 9330 -3.3; 10263 -0.2; 11289 0.0; 12418 0.0; 13660 0.0; 15026 0.0; 16529 0.0; 18182 -0.8; 20000 -3.3
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Stax SR-Lambda Signature GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Stax SR-Lambda Signature ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-8.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.7dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 25 Hz    | 1.98 | 7.1 dB  |
| Peaking | 1744 Hz  | 2.71 | -5.5 dB |
| Peaking | 2493 Hz  | 4.04 | 5.2 dB  |
| Peaking | 5620 Hz  | 7.06 | 3.2 dB  |
| Peaking | 9011 Hz  | 5.8  | -4.0 dB |
| Peaking | 52 Hz    | 2.2  | -3.6 dB |
| Peaking | 112 Hz   | 0.21 | 1.1 dB  |
| Peaking | 560 Hz   | 0.89 | 1.2 dB  |
| Peaking | 1370 Hz  | 4.47 | -1.5 dB |
| Peaking | 10715 Hz | 6.79 | 0.5 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Stax%20SR-Lambda%20Signature/Stax%20SR-Lambda%20Signature.png)