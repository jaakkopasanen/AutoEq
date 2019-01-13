# Audeze LCD-3 sn2312341
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 1.9; 25 1.5; 28 0.7; 31 0.3; 34 0.5; 37 0.6; 41 0.4; 45 0.1; 49 -0.2; 54 -0.4; 60 -0.5; 66 -0.6; 72 -0.7; 79 -1.0; 87 -1.3; 96 -1.8; 106 -1.9; 116 -2.1; 128 -2.5; 141 -2.8; 155 -2.9; 170 -3.1; 187 -3.1; 206 -3.1; 227 -2.9; 249 -2.9; 274 -2.9; 302 -2.7; 332 -2.5; 365 -2.3; 402 -2.4; 442 -2.6; 486 -3.0; 535 -3.1; 588 -2.9; 647 -3.2; 712 -2.5; 783 -1.6; 861 -1.1; 947 -0.3; 1042 0.4; 1146 0.6; 1261 0.8; 1387 0.6; 1526 0.5; 1678 1.0; 1846 1.4; 2031 1.4; 2234 0.8; 2457 0.8; 2703 0.7; 2973 0.8; 3270 0.5; 3597 3.1; 3957 6.0; 4353 5.6; 4788 3.9; 5267 2.3; 5793 0.4; 6373 1.7; 7010 2.0; 7711 0.3; 8482 0.0; 9330 0.0; 10263 0.0; 11289 0.0; 12418 0.0; 13660 0.0; 15026 0.0; 16529 -2.5; 18182 -6.3; 20000 -5.1
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audeze LCD-3 sn2312341 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audeze LCD-3 sn2312341 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.3dB**.

| Type    | Fc       |     Q | Gain    |
|:--------|:---------|:------|:--------|
| Peaking | 15 Hz    |  1    | 3.2 dB  |
| Peaking | 189 Hz   |  0.64 | -3.2 dB |
| Peaking | 578 Hz   |  2.16 | -2.7 dB |
| Peaking | 4209 Hz  |  2.74 | 6.2 dB  |
| Peaking | 18882 Hz |  1.81 | -7.4 dB |
| Peaking | 713 Hz   |  4.02 | -0.9 dB |
| Peaking | 1499 Hz  |  0.99 | 1.1 dB  |
| Peaking | 3170 Hz  |  6.76 | -1.9 dB |
| Peaking | 6848 Hz  | 10.63 | 1.6 dB  |
| Peaking | 10874 Hz |  4.69 | 0.5 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Audeze%20LCD-3%20sn2312341/Audeze%20LCD-3%20sn2312341.png)