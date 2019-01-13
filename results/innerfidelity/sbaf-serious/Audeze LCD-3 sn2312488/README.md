# Audeze LCD-3 sn2312488
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 2.9; 25 2.9; 28 2.8; 31 2.4; 34 2.1; 37 2.0; 41 2.1; 45 2.1; 49 1.7; 54 1.2; 60 1.0; 66 0.9; 72 0.7; 79 0.4; 87 0.1; 96 -0.3; 106 -0.5; 116 -0.7; 128 -1.0; 141 -1.2; 155 -1.4; 170 -1.6; 187 -1.7; 206 -1.9; 227 -1.8; 249 -2.1; 274 -2.1; 302 -2.2; 332 -2.0; 365 -1.5; 402 -1.3; 442 -1.3; 486 -1.8; 535 -2.0; 588 -1.9; 647 -2.2; 712 -2.1; 783 -1.2; 861 -1.0; 947 -0.5; 1042 0.4; 1146 0.6; 1261 1.2; 1387 0.9; 1526 0.2; 1678 0.5; 1846 1.3; 2031 1.9; 2234 1.7; 2457 1.8; 2703 1.2; 2973 1.0; 3270 0.7; 3597 1.9; 3957 3.8; 4353 6.0; 4788 6.0; 5267 5.0; 5793 2.4; 6373 3.6; 7010 2.5; 7711 0.3; 8482 0.0; 9330 0.0; 10263 0.0; 11289 0.0; 12418 0.0; 13660 0.0; 15026 0.0; 16529 -2.0; 18182 -4.7; 20000 -4.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audeze LCD-3 sn2312488 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audeze LCD-3 sn2312488 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.2dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 23 Hz    | 0.5  | 2.9 dB  |
| Peaking | 227 Hz   | 0.73 | -2.2 dB |
| Peaking | 637 Hz   | 2.82 | -1.9 dB |
| Peaking | 4724 Hz  | 1.87 | 6.1 dB  |
| Peaking | 18852 Hz | 1.65 | -5.5 dB |
| Peaking | 2278 Hz  | 2.19 | 1.4 dB  |
| Peaking | 3874 Hz  | 1.14 | -4.5 dB |
| Peaking | 4182 Hz  | 6.09 | 2.7 dB  |
| Peaking | 4728 Hz  | 0.48 | 2.6 dB  |
| Peaking | 8758 Hz  | 2.14 | -1.8 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Audeze%20LCD-3%20sn2312488/Audeze%20LCD-3%20sn2312488.png)