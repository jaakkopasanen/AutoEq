# Sony MDRV-CD3000
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 6.0; 41 6.0; 45 6.0; 49 6.0; 54 5.5; 60 4.6; 66 3.8; 72 3.2; 79 2.8; 87 2.7; 96 2.5; 106 2.1; 116 1.7; 128 1.3; 141 1.1; 155 0.9; 170 1.2; 187 1.1; 206 1.0; 227 1.2; 249 1.2; 274 1.3; 302 1.2; 332 1.1; 365 0.9; 402 1.0; 442 0.9; 486 0.4; 535 0.2; 588 0.8; 647 0.6; 712 0.4; 783 0.5; 861 0.2; 947 -0.0; 1042 0.2; 1146 0.4; 1261 0.7; 1387 0.9; 1526 1.1; 1678 1.2; 1846 1.6; 2031 2.3; 2234 3.1; 2457 3.5; 2703 3.0; 2973 2.6; 3270 1.8; 3597 1.4; 3957 2.7; 4353 0.8; 4788 0.1; 5267 1.4; 5793 0.4; 6373 0.5; 7010 1.6; 7711 0.3; 8482 0.0; 9330 0.0; 10263 0.0; 11289 0.0; 12418 0.0; 13660 0.0; 15026 0.0; 16529 -0.7; 18182 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sony MDRV-CD3000 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony MDRV-CD3000 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc       |     Q | Gain    |
|:--------|:---------|:------|:--------|
| Peaking | 32 Hz    |  0.52 | 6.5 dB  |
| Peaking | 313 Hz   |  1.35 | 0.9 dB  |
| Peaking | 2391 Hz  |  2.8  | 2.2 dB  |
| Peaking | 3021 Hz  |  0.79 | 1.5 dB  |
| Peaking | 16922 Hz |  3.22 | -0.6 dB |
| Peaking | 47 Hz    |  1.25 | -0.8 dB |
| Peaking | 51 Hz    |  2.91 | 1.6 dB  |
| Peaking | 4006 Hz  | 13.77 | 1.7 dB  |
| Peaking | 5810 Hz  |  0.86 | -0.5 dB |
| Peaking | 6907 Hz  |  8.03 | 1.8 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sony%20MDRV-CD3000/Sony%20MDRV-CD3000.png)