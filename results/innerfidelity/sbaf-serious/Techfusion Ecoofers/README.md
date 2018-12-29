# Techfusion Ecoofers
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -1.4dB
GraphicEQ: 21 -14.9; 23 -14.9; 25 -14.9; 28 -15.0; 31 -15.0; 34 -15.0; 37 -15.0; 41 -14.9; 45 -14.9; 49 -14.9; 54 -14.9; 60 -14.9; 66 -14.9; 72 -14.9; 79 -14.9; 87 -15.0; 96 -14.9; 106 -14.8; 116 -14.5; 128 -14.3; 141 -14.0; 155 -13.7; 170 -13.2; 187 -12.7; 206 -12.2; 227 -11.5; 249 -10.9; 274 -10.2; 302 -9.4; 332 -8.6; 365 -7.8; 402 -7.0; 442 -6.0; 486 -5.3; 535 -4.3; 588 -3.3; 647 -2.4; 712 -1.6; 783 -0.6; 861 -0.4; 947 -0.0; 1042 0.0; 1146 0.1; 1261 0.1; 1387 -0.2; 1526 -0.6; 1678 -1.2; 1846 -2.7; 2031 -2.8; 2234 -2.7; 2457 -2.5; 2703 -3.0; 2973 -3.3; 3270 -1.3; 3597 1.0; 3957 0.9; 4353 -0.7; 4788 -1.6; 5267 -1.9; 5793 -3.5; 6373 -5.3; 7010 -3.6; 7711 -0.9; 8482 0.0; 9330 0.0; 10263 0.0; 11289 -0.6; 12418 0.0; 13660 0.0; 15026 0.0; 16529 -1.8; 18182 -2.5; 20000 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Techfusion Ecoofers GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-13**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Techfusion Ecoofers ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-1.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-0.4dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 57 Hz    | 0.09 | -15.4 dB |
| Peaking | 1464 Hz  | 0.3  | 7.7 dB   |
| Peaking | 2271 Hz  | 0.92 | -8.7 dB  |
| Peaking | 6286 Hz  | 2.76 | -6.6 dB  |
| Peaking | 17633 Hz | 2.73 | -3.2 dB  |
| Peaking | 2397 Hz  | 7.36 | 0.9 dB   |
| Peaking | 3074 Hz  | 4.52 | -2.6 dB  |
| Peaking | 3611 Hz  | 3.66 | 2.6 dB   |
| Peaking | 4583 Hz  | 6.01 | -1.6 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Techfusion%20Ecoofers/Techfusion%20Ecoofers.png)