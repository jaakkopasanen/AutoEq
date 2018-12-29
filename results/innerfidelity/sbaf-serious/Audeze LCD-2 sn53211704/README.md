# Audeze LCD-2 sn53211704
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -5.4dB
GraphicEQ: 21 0.0; 23 2.5; 25 2.5; 28 2.5; 31 2.6; 34 2.7; 37 2.7; 41 2.3; 45 2.1; 49 2.2; 54 2.1; 60 1.5; 66 1.1; 72 0.8; 79 0.7; 87 0.4; 96 -0.0; 106 -0.3; 116 -0.5; 128 -0.9; 141 -0.9; 155 -1.3; 170 -1.4; 187 -1.5; 206 -1.8; 227 -1.9; 249 -2.0; 274 -2.0; 302 -2.0; 332 -2.0; 365 -1.7; 402 -1.4; 442 -1.0; 486 -0.9; 535 -1.0; 588 -1.1; 647 -1.5; 712 -2.2; 783 -2.2; 861 -2.3; 947 -1.0; 1042 0.6; 1146 0.8; 1261 1.0; 1387 0.0; 1526 -0.8; 1678 -0.3; 1846 0.8; 2031 1.3; 2234 1.4; 2457 2.0; 2703 2.4; 2973 2.5; 3270 3.0; 3597 4.1; 3957 5.3; 4353 4.6; 4788 4.0; 5267 2.9; 5793 1.6; 6373 4.3; 7010 2.5; 7711 0.3; 8482 -0.5; 9330 0.0; 10263 0.0; 11289 0.0; 12418 0.0; 13660 0.0; 15026 0.0; 16529 -0.9; 18182 -4.6; 20000 -4.7
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audeze LCD-2 sn53211704 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-53**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audeze LCD-2 sn53211704 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.1dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 32 Hz    | 0.6  | 2.8 dB  |
| Peaking | 238 Hz   | 0.71 | -2.2 dB |
| Peaking | 781 Hz   | 3.86 | -2.3 dB |
| Peaking | 3970 Hz  | 1.59 | 5.0 dB  |
| Peaking | 6570 Hz  | 9.17 | 3.5 dB  |
| Peaking | 1217 Hz  | 2.73 | 3.2 dB  |
| Peaking | 1499 Hz  | 1.33 | -3.2 dB |
| Peaking | 1988 Hz  | 1.8  | 2.2 dB  |
| Peaking | 8358 Hz  | 6.61 | -1.0 dB |
| Peaking | 19148 Hz | 1.84 | -5.9 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Audeze%20LCD-2%20sn53211704/Audeze%20LCD-2%20sn53211704.png)