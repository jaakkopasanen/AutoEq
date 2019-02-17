# Sony MDRV-CD3000
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -1.0; 60 -1.9; 66 -2.7; 72 -3.3; 79 -3.7; 87 -3.8; 96 -4.0; 106 -4.4; 116 -4.8; 128 -5.2; 141 -5.4; 155 -5.6; 170 -5.3; 187 -5.4; 206 -5.5; 227 -5.3; 249 -5.3; 274 -5.2; 302 -5.3; 332 -5.4; 365 -5.6; 402 -5.5; 442 -5.6; 486 -6.1; 535 -6.3; 588 -5.7; 647 -5.9; 712 -6.1; 783 -6.0; 861 -6.3; 947 -6.5; 1042 -6.3; 1146 -6.1; 1261 -5.8; 1387 -5.6; 1526 -5.4; 1678 -5.3; 1846 -4.9; 2031 -4.2; 2234 -3.4; 2457 -3.0; 2703 -3.5; 2973 -3.9; 3270 -4.7; 3597 -5.1; 3957 -3.8; 4353 -5.7; 4788 -6.4; 5267 -5.1; 5793 -6.1; 6373 -6.0; 7010 -4.9; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -7.2; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sony MDRV-CD3000 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony MDRV-CD3000 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 32 Hz    | 0.52 | 6.5 dB  |
| Peaking | 314 Hz   | 1.32 | 0.9 dB  |
| Peaking | 2409 Hz  | 2.16 | 2.6 dB  |
| Peaking | 3395 Hz  | 0.72 | 1.1 dB  |
| Peaking | 16620 Hz | 3.04 | -0.7 dB |
| Peaking | 48 Hz    | 1.18 | -0.9 dB |
| Peaking | 52 Hz    | 2.97 | 1.6 dB  |
| Peaking | 6962 Hz  | 6.7  | 2.3 dB  |
| Peaking | 6972 Hz  | 2.27 | -1.0 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.9 dB  |
| Peaking | 62 Hz    | 1.41 | 3.3 dB  |
| Peaking | 125 Hz   | 1.41 | 0.4 dB  |
| Peaking | 250 Hz   | 1.41 | 0.9 dB  |
| Peaking | 500 Hz   | 1.41 | 0.5 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.6 dB |
| Peaking | 2000 Hz  | 1.41 | 2.5 dB  |
| Peaking | 4000 Hz  | 1.41 | 1.3 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.1 dB  |
| Peaking | 16000 Hz | 1.41 | -0.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sony%20MDRV-CD3000/Sony%20MDRV-CD3000.png)