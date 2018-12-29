# Sennheiser Momentum On-Ear
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 -3.5; 23 -3.7; 25 -3.8; 28 -3.9; 31 -4.1; 34 -4.2; 37 -4.3; 41 -4.4; 45 -4.4; 49 -4.5; 54 -4.5; 60 -4.5; 66 -4.5; 72 -4.4; 79 -4.4; 87 -4.5; 96 -4.6; 106 -4.6; 116 -4.5; 128 -4.6; 141 -4.4; 155 -4.2; 170 -3.7; 187 -3.3; 206 -2.8; 227 -2.0; 249 -1.1; 274 -0.2; 302 0.7; 332 1.2; 365 1.5; 402 1.7; 442 1.9; 486 1.6; 535 1.3; 588 1.0; 647 0.4; 712 -0.2; 783 -0.1; 861 0.1; 947 0.2; 1042 -0.2; 1146 -1.0; 1261 -2.1; 1387 -3.3; 1526 -4.4; 1678 -5.2; 1846 -5.4; 2031 -4.4; 2234 -3.3; 2457 -1.3; 2703 0.5; 2973 2.1; 3270 3.4; 3597 4.8; 3957 6.0; 4353 6.0; 4788 1.2; 5267 1.5; 5793 2.8; 6373 1.3; 7010 -0.7; 7711 -1.0; 8482 -2.0; 9330 -2.4; 10263 -0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser Momentum On-Ear GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser Momentum On-Ear ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.2dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 43 Hz    | 0.53 | -4.6 dB |
| Peaking | 134 Hz   | 1.55 | -3.4 dB |
| Peaking | 1811 Hz  | 2.13 | -6.4 dB |
| Peaking | 3885 Hz  | 2.1  | 6.6 dB  |
| Peaking | 8773 Hz  | 4.01 | -2.9 dB |
| Peaking | 12 Hz    | 2    | -1.0 dB |
| Peaking | 206 Hz   | 3    | -1.3 dB |
| Peaking | 326 Hz   | 2.48 | 1.1 dB  |
| Peaking | 455 Hz   | 1.77 | 2.0 dB  |
| Peaking | 24000 Hz | 1.97 | -0.1 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sennheiser%20Momentum%20On-Ear/Sennheiser%20Momentum%20On-Ear.png)