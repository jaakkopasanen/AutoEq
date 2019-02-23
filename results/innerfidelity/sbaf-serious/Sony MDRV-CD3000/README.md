# Sony MDRV-CD3000
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -1.2; 54 -2.1; 60 -3.1; 66 -3.9; 72 -4.5; 79 -4.8; 87 -5.0; 96 -5.2; 106 -5.6; 116 -6.0; 128 -6.4; 141 -6.6; 155 -6.8; 170 -6.5; 187 -6.6; 206 -6.7; 227 -6.5; 249 -6.5; 274 -6.4; 302 -6.5; 332 -6.6; 365 -6.8; 402 -6.7; 442 -6.8; 486 -7.3; 535 -7.5; 588 -6.8; 647 -7.1; 712 -7.3; 783 -7.2; 861 -7.5; 947 -7.7; 1042 -7.5; 1146 -7.3; 1261 -7.0; 1387 -6.8; 1526 -6.6; 1678 -6.5; 1846 -6.1; 2031 -5.4; 2234 -4.6; 2457 -4.2; 2703 -4.7; 2973 -5.1; 3270 -5.9; 3597 -6.3; 3957 -5.0; 4353 -6.8; 4788 -7.6; 5267 -6.3; 5793 -7.3; 6373 -7.2; 7010 -6.0; 7711 -6.3; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.6; 16529 -8.4; 18182 -6.8; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sony MDRV-CD3000 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony MDRV-CD3000 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 0.74 | 6.7 dB  |
| Peaking | 1299 Hz  | 0.3  | -1.0 dB |
| Peaking | 2373 Hz  | 2.28 | 0.7 dB  |
| Peaking | 2474 Hz  | 1.64 | 2.4 dB  |
| Peaking | 16786 Hz | 3.28 | -2.2 dB |
| Peaking | 47 Hz    | 4.42 | 1.1 dB  |
| Peaking | 142 Hz   | 2.82 | -0.7 dB |
| Peaking | 4034 Hz  | 7.98 | 2.6 dB  |
| Peaking | 4355 Hz  | 3.37 | -1.5 dB |
| Peaking | 7247 Hz  | 6.82 | 0.7 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 7.3 dB  |
| Peaking | 62 Hz    | 1.41 | 2.2 dB  |
| Peaking | 125 Hz   | 1.41 | -0.5 dB |
| Peaking | 250 Hz   | 1.41 | 0.0 dB  |
| Peaking | 500 Hz   | 1.41 | -0.4 dB |
| Peaking | 1000 Hz  | 1.41 | -1.5 dB |
| Peaking | 2000 Hz  | 1.41 | 1.7 dB  |
| Peaking | 4000 Hz  | 1.41 | 0.1 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.0 dB |
| Peaking | 16000 Hz | 1.41 | -1.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sony%20MDRV-CD3000/Sony%20MDRV-CD3000.png)