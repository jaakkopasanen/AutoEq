# Zoukbox ZLX30
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -5.7dB
GraphicEQ: 21 -9.8; 23 -9.8; 25 -9.7; 28 -9.7; 31 -9.7; 34 -9.6; 37 -9.5; 41 -9.4; 45 -9.3; 49 -9.2; 54 -9.1; 60 -9.0; 66 -8.9; 72 -8.8; 79 -8.8; 87 -8.7; 96 -8.6; 106 -8.4; 116 -8.0; 128 -7.8; 141 -7.5; 155 -7.1; 170 -6.7; 187 -6.3; 206 -5.8; 227 -5.2; 249 -4.7; 274 -4.1; 302 -3.5; 332 -3.0; 365 -2.3; 402 -1.8; 442 -1.2; 486 -0.8; 535 -0.3; 588 0.3; 647 0.6; 712 0.7; 783 1.1; 861 0.8; 947 0.3; 1042 -0.2; 1146 -0.7; 1261 -1.3; 1387 -2.3; 1526 -3.5; 1678 -4.6; 1846 -5.6; 2031 -6.5; 2234 -7.5; 2457 -7.2; 2703 -5.3; 2973 -1.9; 3270 -1.1; 3597 -3.3; 3957 -7.4; 4353 -10.0; 4788 -5.7; 5267 2.9; 5793 5.4; 6373 5.4; 7010 2.5; 7711 0.3; 8482 0.0; 9330 0.0; 10263 -2.6; 11289 -0.7; 12418 0.0; 13660 0.0; 15026 -0.8; 16529 -2.4; 18182 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Zoukbox ZLX30 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-56**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Zoukbox ZLX30 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.5dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 28 Hz    | 0.25 | -9.6 dB  |
| Peaking | 153 Hz   | 0.81 | -3.8 dB  |
| Peaking | 2163 Hz  | 2.18 | -7.7 dB  |
| Peaking | 4372 Hz  | 4.51 | -12.0 dB |
| Peaking | 5839 Hz  | 3.28 | 8.2 dB   |
| Peaking | 763 Hz   | 1.98 | 1.9 dB   |
| Peaking | 1554 Hz  | 4.04 | -1.5 dB  |
| Peaking | 10470 Hz | 6.45 | -3.3 dB  |
| Peaking | 12766 Hz | 0.09 | 0.2 dB   |
| Peaking | 16053 Hz | 4.39 | -3.2 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Zoukbox%20ZLX30/Zoukbox%20ZLX30.png)