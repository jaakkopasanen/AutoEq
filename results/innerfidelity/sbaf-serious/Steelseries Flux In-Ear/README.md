# Steelseries Flux In-Ear
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -1.9dB
GraphicEQ: 21 -5.4; 23 -5.4; 25 -5.4; 28 -5.4; 31 -5.5; 34 -5.5; 37 -5.6; 41 -5.6; 45 -5.6; 49 -5.7; 54 -5.8; 60 -5.9; 66 -6.1; 72 -6.2; 79 -6.4; 87 -6.5; 96 -6.7; 106 -6.7; 116 -6.6; 128 -6.6; 141 -6.5; 155 -6.3; 170 -6.1; 187 -5.8; 206 -5.5; 227 -5.0; 249 -4.7; 274 -4.2; 302 -3.7; 332 -3.2; 365 -2.7; 402 -2.2; 442 -1.6; 486 -1.3; 535 -0.8; 588 -0.2; 647 0.2; 712 0.3; 783 0.6; 861 0.5; 947 0.2; 1042 -0.2; 1146 -0.6; 1261 -1.1; 1387 -1.9; 1526 -2.6; 1678 -3.1; 1846 -3.4; 2031 -3.5; 2234 -4.0; 2457 -3.6; 2703 -3.4; 2973 -3.2; 3270 -0.5; 3597 1.3; 3957 1.6; 4353 0.3; 4788 0.1; 5267 0.9; 5793 0.7; 6373 -0.5; 7010 -0.2; 7711 0.3; 8482 0.0; 9330 0.0; 10263 0.0; 11289 0.0; 12418 0.0; 13660 -1.7; 15026 -2.8; 16529 -2.2; 18182 -2.4; 20000 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Steelseries Flux In-Ear GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-18**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Steelseries Flux In-Ear ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-2.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-1.9dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 36 Hz    | 0.25 | -5.4 dB |
| Peaking | 165 Hz   | 0.73 | -3.9 dB |
| Peaking | 2330 Hz  | 1.44 | -4.5 dB |
| Peaking | 3789 Hz  | 3.23 | 3.2 dB  |
| Peaking | 16455 Hz | 1.48 | -2.9 dB |
| Peaking | 331 Hz   | 1.56 | -0.9 dB |
| Peaking | 776 Hz   | 1.67 | 1.2 dB  |
| Peaking | 1550 Hz  | 2.95 | -1.4 dB |
| Peaking | 1664 Hz  | 0.12 | 0.4 dB  |
| Peaking | 2929 Hz  | 9.62 | -1.7 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Steelseries%20Flux%20In-Ear/Steelseries%20Flux%20In-Ear.png)