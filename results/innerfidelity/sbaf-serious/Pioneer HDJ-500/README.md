# Pioneer HDJ-500
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 6.0; 41 6.0; 45 5.6; 49 4.7; 54 3.7; 60 2.9; 66 2.6; 72 2.5; 79 2.1; 87 1.8; 96 1.8; 106 1.6; 116 1.4; 128 1.1; 141 0.9; 155 0.5; 170 0.6; 187 0.3; 206 0.1; 227 0.2; 249 0.4; 274 0.3; 302 0.1; 332 0.1; 365 -0.6; 402 -0.4; 442 0.1; 486 -0.4; 535 -0.8; 588 -0.7; 647 -0.7; 712 -0.7; 783 -0.5; 861 -0.3; 947 -0.3; 1042 0.2; 1146 0.7; 1261 1.4; 1387 1.7; 1526 2.3; 1678 3.0; 1846 4.4; 2031 5.8; 2234 6.0; 2457 6.0; 2703 6.0; 2973 6.0; 3270 6.0; 3597 6.0; 3957 6.0; 4353 6.0; 4788 1.2; 5267 -2.1; 5793 -0.8; 6373 -0.4; 7010 -0.0; 7711 0.3; 8482 0.0; 9330 0.0; 10263 0.0; 11289 0.0; 12418 0.0; 13660 0.0; 15026 -0.2; 16529 -1.6; 18182 -0.5; 20000 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Pioneer HDJ-500 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Pioneer HDJ-500 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 29 Hz    | 0.58 | 6.4 dB  |
| Peaking | 899 Hz   | 0.79 | -2.2 dB |
| Peaking | 3598 Hz  | 0.52 | 8.8 dB  |
| Peaking | 5280 Hz  | 5.44 | -6.3 dB |
| Peaking | 6885 Hz  | 0.79 | -4.5 dB |
| Peaking | 2102 Hz  | 4.88 | 1.5 dB  |
| Peaking | 4116 Hz  | 0.61 | -0.8 dB |
| Peaking | 4398 Hz  | 7.39 | 2.7 dB  |
| Peaking | 8523 Hz  | 2.06 | 0.8 dB  |
| Peaking | 16772 Hz | 3.4  | -1.9 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Pioneer%20HDJ-500/Pioneer%20HDJ-500.png)