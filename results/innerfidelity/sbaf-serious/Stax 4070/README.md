# Stax 4070
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -3.2dB
GraphicEQ: 21 0.0; 23 1.0; 25 0.1; 28 -0.5; 31 -0.6; 34 -0.4; 37 -0.1; 41 0.3; 45 0.6; 49 0.9; 54 1.1; 60 1.2; 66 1.1; 72 0.9; 79 0.8; 87 0.6; 96 0.4; 106 0.3; 116 0.2; 128 -0.1; 141 -0.2; 155 -0.4; 170 -0.3; 187 -0.6; 206 -0.7; 227 -0.7; 249 -0.8; 274 -1.0; 302 -1.0; 332 -1.0; 365 -0.1; 402 1.6; 442 2.2; 486 1.4; 535 1.4; 588 1.9; 647 2.0; 712 1.4; 783 1.2; 861 0.5; 947 0.1; 1042 -0.2; 1146 -0.5; 1261 -1.0; 1387 -1.8; 1526 -3.2; 1678 -4.1; 1846 -4.0; 2031 -3.5; 2234 -2.7; 2457 -2.0; 2703 -2.6; 2973 -3.7; 3270 -4.0; 3597 -5.1; 3957 -6.4; 4353 -7.0; 4788 -4.5; 5267 -1.6; 5793 -1.2; 6373 -0.5; 7010 2.3; 7711 0.3; 8482 -1.4; 9330 -3.0; 10263 -1.3; 11289 -0.6; 12418 -0.6; 13660 -0.2; 15026 0.0; 16529 0.0; 18182 -0.0; 20000 -3.2
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Stax 4070 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-32**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Stax 4070 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-2.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-2.2dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 62 Hz    | 2.32 | 1.3 dB  |
| Peaking | 620 Hz   | 1.79 | 2.3 dB  |
| Peaking | 1790 Hz  | 1.9  | -4.0 dB |
| Peaking | 4056 Hz  | 2.67 | -7.0 dB |
| Peaking | 9323 Hz  | 7.02 | -3.1 dB |
| Peaking | 91 Hz    | 3.08 | 0.3 dB  |
| Peaking | 304 Hz   | 1.33 | -1.5 dB |
| Peaking | 423 Hz   | 4.96 | 2.4 dB  |
| Peaking | 6977 Hz  | 7.02 | 3.7 dB  |
| Peaking | 20626 Hz | 0.06 | -0.4 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Stax%204070/Stax%204070.png)