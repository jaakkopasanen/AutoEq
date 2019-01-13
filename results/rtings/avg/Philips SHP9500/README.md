# Philips SHP9500
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 5.9; 41 5.3; 45 4.6; 49 3.9; 54 3.2; 60 2.4; 66 1.6; 72 1.0; 79 0.5; 87 -0.0; 96 -0.5; 106 -0.9; 116 -1.2; 128 -1.4; 141 -1.3; 155 -1.3; 170 -1.2; 187 -1.1; 206 -0.8; 227 -0.4; 249 -0.2; 274 -0.0; 302 -0.0; 332 -0.0; 365 0.1; 402 -0.1; 442 -0.2; 486 -0.2; 535 -0.2; 588 -0.2; 647 -0.1; 712 -0.0; 783 -0.0; 861 0.0; 947 -0.0; 1042 0.0; 1146 -0.1; 1261 -0.6; 1387 -1.0; 1526 -0.9; 1678 -0.7; 1846 -0.5; 2031 0.3; 2234 1.3; 2457 1.1; 2703 -0.6; 2973 -1.6; 3270 -1.7; 3597 -2.2; 3957 -4.1; 4353 -4.4; 4788 -4.5; 5267 -4.3; 5793 -4.8; 6373 -2.4; 7010 -0.1; 7711 -0.3; 8482 -2.1; 9330 -2.8; 10263 -0.3; 11289 0.0; 12418 0.0; 13660 0.0; 15026 0.0; 16529 -0.3; 18182 -4.5; 20000 -3.2
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Philips SHP9500 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Philips SHP9500 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.5dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 28 Hz    | 0.59 | 6.5 dB  |
| Peaking | 115 Hz   | 0.93 | -2.4 dB |
| Peaking | 4865 Hz  | 1.72 | -5.0 dB |
| Peaking | 18346 Hz | 3.4  | -4.0 dB |
| Peaking | 19648 Hz | 2.77 | -3.3 dB |
| Peaking | 1460 Hz  | 4.42 | -0.8 dB |
| Peaking | 2334 Hz  | 3.92 | 3.2 dB  |
| Peaking | 2549 Hz  | 1.52 | -1.1 dB |
| Peaking | 7266 Hz  | 6.99 | 2.1 dB  |
| Peaking | 9043 Hz  | 6.71 | -2.6 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Philips%20SHP9500/Philips%20SHP9500.png)