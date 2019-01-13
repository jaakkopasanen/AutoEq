# Jays A Jays 5
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -1.0dB
GraphicEQ: 21 -2.9; 23 -3.2; 25 -3.5; 28 -3.9; 31 -4.1; 34 -4.3; 37 -4.5; 41 -4.7; 45 -4.9; 49 -5.0; 54 -5.1; 60 -5.3; 66 -5.4; 72 -5.6; 79 -5.8; 87 -5.9; 96 -6.1; 106 -6.0; 116 -6.0; 128 -5.9; 141 -5.7; 155 -5.6; 170 -5.3; 187 -5.0; 206 -4.6; 227 -4.2; 249 -3.8; 274 -3.3; 302 -2.8; 332 -2.4; 365 -1.9; 402 -1.4; 442 -0.8; 486 -0.5; 535 -0.2; 588 0.4; 647 0.6; 712 0.8; 783 0.9; 861 0.7; 947 0.3; 1042 -0.2; 1146 -0.6; 1261 -1.2; 1387 -2.1; 1526 -3.1; 1678 -4.0; 1846 -4.7; 2031 -5.4; 2234 -6.6; 2457 -7.9; 2703 -8.5; 2973 -6.0; 3270 -2.3; 3597 0.1; 3957 0.2; 4353 -1.9; 4788 -3.6; 5267 -5.1; 5793 -7.4; 6373 -6.2; 7010 -2.8; 7711 -1.3; 8482 -2.0; 9330 -2.2; 10263 -0.8; 11289 0.0; 12418 0.0; 13660 0.0; 15026 -0.0; 16529 -2.0; 18182 -0.5; 20000 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Jays A Jays 5 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-10**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Jays A Jays 5 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-1.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-0.1dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 46 Hz    | 0.46 | -4.3 dB |
| Peaking | 122 Hz   | 0.95 | -3.7 dB |
| Peaking | 229 Hz   | 1.6  | -2.2 dB |
| Peaking | 2413 Hz  | 2.11 | -8.3 dB |
| Peaking | 5933 Hz  | 3.52 | -7.4 dB |
| Peaking | 764 Hz   | 1.98 | 1.6 dB  |
| Peaking | 1590 Hz  | 4.2  | -1.7 dB |
| Peaking | 2841 Hz  | 9.45 | -2.6 dB |
| Peaking | 3686 Hz  | 4.91 | 3.4 dB  |
| Peaking | 16762 Hz | 0.18 | -0.5 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Jays%20A%20Jays%205/Jays%20A%20Jays%205.png)