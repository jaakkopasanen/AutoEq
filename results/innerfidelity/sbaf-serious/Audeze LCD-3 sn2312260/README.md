# Audeze LCD-3 sn2312260

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 1.5; 25 1.2; 28 0.5; 31 0.0; 34 -0.0; 37 -0.0; 41 -0.2; 45 -0.3; 49 -0.5; 54 -0.6; 60 -0.7; 66 -0.9; 72 -1.3; 79 -1.5; 87 -1.8; 96 -2.2; 106 -2.4; 116 -2.7; 128 -3.0; 141 -3.1; 155 -3.3; 170 -3.6; 187 -3.8; 206 -4.0; 227 -3.9; 249 -3.7; 274 -3.4; 302 -2.9; 332 -2.5; 365 -2.3; 402 -2.9; 442 -3.4; 486 -3.7; 535 -3.6; 588 -3.4; 647 -2.9; 712 -2.4; 783 -2.2; 861 -1.8; 947 -0.7; 1042 0.3; 1146 0.4; 1261 0.2; 1387 -0.2; 1526 -0.1; 1678 0.5; 1846 1.3; 2031 1.5; 2234 1.5; 2457 1.4; 2703 1.4; 2973 -0.1; 3270 1.3; 3597 5.7; 3957 5.9; 4353 3.9; 4788 2.5; 5267 0.3; 5793 -1.9; 6373 -0.5; 7010 0.8; 7711 0.3; 8482 0.0; 9330 0.0; 10263 0.0; 11289 0.0; 12418 -0.2; 13660 -1.7; 15026 -1.7; 16529 -4.7; 18182 -6.7; 20000 -1.8
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audeze LCD-3 sn2312260 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audeze LCD-3 sn2312260 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 191 Hz   | 0.67 | -3.8 dB |
| Peaking | 346 Hz   | 2.83 | 0.5 dB  |
| Peaking | 545 Hz   | 1.76 | -2.9 dB |
| Peaking | 3885 Hz  | 3.72 | 6.6 dB  |
| Peaking | 18017 Hz | 1.6  | -7.2 dB |
| Peaking | 22 Hz    | 1.86 | 1.5 dB  |
| Peaking | 1096 Hz  | 7.57 | 1.1 dB  |
| Peaking | 1924 Hz  | 5.54 | 1.3 dB  |
| Peaking | 2473 Hz  | 2.83 | 1.2 dB  |
| Peaking | 3074 Hz  | 8.99 | -2.5 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Audeze%20LCD-3%20sn2312260/Audeze%20LCD-3%20sn2312260.png)