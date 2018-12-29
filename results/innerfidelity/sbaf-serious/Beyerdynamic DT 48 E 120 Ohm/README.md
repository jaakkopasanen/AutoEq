# Beyerdynamic DT 48 E 120 Ohm
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.3dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 6.0; 41 6.0; 45 6.0; 49 6.0; 54 6.0; 60 6.0; 66 4.6; 72 -2.6; 79 -7.2; 87 -4.7; 96 -2.9; 106 -4.2; 116 -3.8; 128 -3.2; 141 -2.6; 155 -1.7; 170 -2.3; 187 -2.2; 206 -1.8; 227 -1.1; 249 -0.6; 274 0.2; 302 0.8; 332 1.2; 365 1.6; 402 2.3; 442 3.2; 486 4.0; 535 5.1; 588 6.0; 647 5.9; 712 4.8; 783 3.3; 861 1.9; 947 1.0; 1042 -0.8; 1146 -2.9; 1261 -3.9; 1387 -4.7; 1526 -5.5; 1678 -6.5; 1846 -6.2; 2031 -6.0; 2234 -4.7; 2457 -2.0; 2703 0.8; 2973 2.1; 3270 2.6; 3597 4.2; 3957 6.0; 4353 6.0; 4788 6.0; 5267 6.0; 5793 6.0; 6373 5.5; 7010 1.5; 7711 -5.3; 8482 -8.4; 9330 -5.3; 10263 -0.6; 11289 0.0; 12418 0.0; 13660 0.0; 15026 -4.6; 16529 -9.9; 18182 -11.0; 20000 -4.2
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Beyerdynamic DT 48 E 120 Ohm GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-62**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beyerdynamic DT 48 E 120 Ohm ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-8.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.7dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 33 Hz    | 1.6  | 7.5 dB   |
| Peaking | 1799 Hz  | 1.05 | -17.6 dB |
| Peaking | 4211 Hz  | 0.15 | 11.3 dB  |
| Peaking | 8493 Hz  | 2.88 | -16.7 dB |
| Peaking | 17420 Hz | 0.95 | -16.4 dB |
| Peaking | 63 Hz    | 2.34 | 7.5 dB   |
| Peaking | 77 Hz    | 4.4  | -10.5 dB |
| Peaking | 114 Hz   | 2.18 | -3.9 dB  |
| Peaking | 196 Hz   | 1.64 | -2.5 dB  |
| Peaking | 599 Hz   | 3.09 | 4.3 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Beyerdynamic%20DT%2048%20E%20120%20Ohm/Beyerdynamic%20DT%2048%20E%20120%20Ohm.png)