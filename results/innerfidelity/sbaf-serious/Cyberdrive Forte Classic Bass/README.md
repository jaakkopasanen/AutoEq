# Cyberdrive Forte Classic Bass
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -3.5dB
GraphicEQ: 21 -12.1; 23 -12.2; 25 -12.2; 28 -12.2; 31 -12.3; 34 -12.2; 37 -12.2; 41 -12.2; 45 -12.2; 49 -12.2; 54 -12.2; 60 -12.2; 66 -12.3; 72 -12.3; 79 -12.4; 87 -12.4; 96 -12.4; 106 -12.3; 116 -12.1; 128 -11.9; 141 -11.6; 155 -11.3; 170 -10.9; 187 -10.4; 206 -9.9; 227 -9.2; 249 -8.7; 274 -8.0; 302 -7.2; 332 -6.5; 365 -5.8; 402 -5.0; 442 -4.2; 486 -3.6; 535 -2.8; 588 -1.9; 647 -1.4; 712 -1.1; 783 -0.0; 861 -0.3; 947 -0.3; 1042 -0.3; 1146 -0.4; 1261 -0.4; 1387 -0.6; 1526 -0.8; 1678 -0.6; 1846 0.1; 2031 0.9; 2234 1.7; 2457 2.7; 2703 3.2; 2973 3.4; 3270 3.0; 3597 1.5; 3957 -1.1; 4353 -4.1; 4788 -5.4; 5267 -6.0; 5793 -9.2; 6373 -13.0; 7010 -8.8; 7711 -5.1; 8482 -4.1; 9330 -4.8; 10263 -4.2; 11289 -0.9; 12418 0.0; 13660 0.0; 15026 -0.2; 16529 -3.7; 18182 -3.2; 20000 -0.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Cyberdrive Forte Classic Bass GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-35**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Cyberdrive Forte Classic Bass ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-3.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-1.6dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 59 Hz    | 0.13 | -12.9 dB |
| Peaking | 3471 Hz  | 0.08 | 2.9 dB   |
| Peaking | 6256 Hz  | 2.13 | -15.0 dB |
| Peaking | 9839 Hz  | 3.6  | -4.7 dB  |
| Peaking | 17417 Hz | 1.58 | -5.8 dB  |
| Peaking | 16 Hz    | 2.11 | -1.2 dB  |
| Peaking | 724 Hz   | 1.49 | 1.1 dB   |
| Peaking | 1651 Hz  | 1.27 | -3.0 dB  |
| Peaking | 3052 Hz  | 1.2  | 3.6 dB   |
| Peaking | 4382 Hz  | 4.07 | -4.2 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Cyberdrive%20Forte%20Classic%20Bass/Cyberdrive%20Forte%20Classic%20Bass.png)