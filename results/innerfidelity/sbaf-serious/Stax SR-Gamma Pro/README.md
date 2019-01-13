# Stax SR-Gamma Pro
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 6.0; 41 6.0; 45 6.0; 49 6.0; 54 6.0; 60 5.3; 66 3.8; 72 3.2; 79 2.5; 87 1.6; 96 0.4; 106 -0.1; 116 -0.6; 128 -1.2; 141 -1.2; 155 -1.2; 170 -1.1; 187 -1.2; 206 -1.2; 227 -0.9; 249 -0.5; 274 -0.1; 302 0.3; 332 0.5; 365 0.6; 402 0.6; 442 0.8; 486 0.6; 535 0.6; 588 0.8; 647 0.9; 712 0.6; 783 0.7; 861 0.3; 947 0.2; 1042 -0.1; 1146 -0.3; 1261 -0.9; 1387 -1.6; 1526 -2.2; 1678 -2.5; 1846 -2.4; 2031 -1.3; 2234 0.0; 2457 2.3; 2703 3.5; 2973 4.0; 3270 3.9; 3597 3.8; 3957 4.2; 4353 2.6; 4788 1.7; 5267 0.3; 5793 -1.3; 6373 -2.1; 7010 -0.8; 7711 -0.8; 8482 -3.5; 9330 -5.0; 10263 -1.0; 11289 0.0; 12418 0.0; 13660 0.0; 15026 0.0; 16529 0.0; 18182 -0.5; 20000 -4.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Stax SR-Gamma Pro GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Stax SR-Gamma Pro ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.3dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 35 Hz   | 0.9  | 7.2 dB  |
| Peaking | 1809 Hz | 1.26 | -8.7 dB |
| Peaking | 2651 Hz | 0.58 | 7.5 dB  |
| Peaking | 5992 Hz | 2.53 | -4.3 dB |
| Peaking | 9111 Hz | 4.44 | -6.2 dB |
| Peaking | 35 Hz   | 1.45 | -6.2 dB |
| Peaking | 41 Hz   | 0.42 | 5.7 dB  |
| Peaking | 120 Hz  | 0.64 | -4.1 dB |
| Peaking | 380 Hz  | 1.11 | 1.0 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Stax%20SR-Gamma%20Pro/Stax%20SR-Gamma%20Pro.png)