# Beats Solo3 Wireless
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -2.0dB
GraphicEQ: 21 -4.9; 23 -5.3; 25 -5.5; 28 -5.8; 31 -6.0; 34 -6.1; 37 -6.2; 41 -6.3; 45 -6.4; 49 -6.5; 54 -6.6; 60 -6.8; 66 -6.9; 72 -7.0; 79 -7.2; 87 -7.4; 96 -7.8; 106 -8.1; 116 -8.0; 128 -8.1; 141 -8.4; 155 -8.6; 170 -8.1; 187 -8.3; 206 -8.1; 227 -7.7; 249 -7.2; 274 -6.4; 302 -5.6; 332 -5.0; 365 -4.4; 402 -3.2; 442 -2.6; 486 -2.5; 535 -2.0; 588 -1.0; 647 -0.4; 712 0.0; 783 0.5; 861 0.3; 947 0.2; 1042 -0.1; 1146 -0.4; 1261 -0.8; 1387 -1.4; 1526 -1.8; 1678 -1.9; 1846 -1.7; 2031 -1.1; 2234 -0.9; 2457 -0.6; 2703 -0.9; 2973 -1.4; 3270 -2.2; 3597 -2.7; 3957 -0.8; 4353 -1.8; 4788 -2.6; 5267 -0.2; 5793 1.9; 6373 0.8; 7010 1.3; 7711 0.3; 8482 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Beats Solo3 Wireless GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-20**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beats Solo3 Wireless ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-1.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-0.1dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 40 Hz   | 0.33 | -5.7 dB |
| Peaking | 139 Hz  | 0.83 | -4.4 dB |
| Peaking | 251 Hz  | 1.18 | -4.0 dB |
| Peaking | 1665 Hz | 3.46 | -1.9 dB |
| Peaking | 3498 Hz | 2.75 | -2.4 dB |
| Peaking | 490 Hz  | 2.6  | -0.6 dB |
| Peaking | 769 Hz  | 2.57 | 1.4 dB  |
| Peaking | 4792 Hz | 6.05 | -3.6 dB |
| Peaking | 5708 Hz | 2.47 | 2.3 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Beats%20Solo3%20Wireless/Beats%20Solo3%20Wireless.png)