# Blue MOFI Active On
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -6.0; 23 -6.2; 25 -6.5; 28 -6.7; 31 -7.0; 34 -7.1; 37 -7.3; 41 -7.4; 45 -7.5; 49 -7.6; 54 -7.8; 60 -8.0; 66 -8.2; 72 -8.4; 79 -8.7; 87 -9.0; 96 -9.5; 106 -9.6; 116 -9.5; 128 -9.7; 141 -10.4; 155 -10.8; 170 -9.9; 187 -10.5; 206 -10.5; 227 -10.1; 249 -9.4; 274 -8.4; 302 -7.5; 332 -7.3; 365 -7.4; 402 -7.4; 442 -5.5; 486 -5.2; 535 -5.6; 588 -5.8; 647 -6.2; 712 -6.8; 783 -7.1; 861 -7.7; 947 -8.3; 1042 -8.7; 1146 -8.8; 1261 -8.7; 1387 -8.9; 1526 -9.2; 1678 -9.1; 1846 -8.5; 2031 -7.3; 2234 -6.4; 2457 -6.2; 2703 -5.1; 2973 -4.5; 3270 -4.2; 3597 -3.1; 3957 -5.1; 4353 -8.8; 4788 -3.8; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -3.9; 7711 -6.2; 8482 -6.6; 9330 -8.6; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Blue MOFI Active On GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Blue MOFI Active On ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.1dB**.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 111 Hz  |  0.9  | -3.0 dB |
| Peaking | 202 Hz  |  2.14 | -3.0 dB |
| Peaking | 1422 Hz |  1.59 | -3.0 dB |
| Peaking | 3258 Hz |  3.37 | 2.9 dB  |
| Peaking | 5806 Hz |  3.69 | 7.0 dB  |
| Peaking | 506 Hz  |  3.34 | 1.8 dB  |
| Peaking | 978 Hz  |  5.69 | -1.0 dB |
| Peaking | 4276 Hz | 14.72 | -5.1 dB |
| Peaking | 9085 Hz |  6.98 | -2.6 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -0.1 dB |
| Peaking | 62 Hz    | 1.41 | -1.1 dB |
| Peaking | 125 Hz   | 1.41 | -3.4 dB |
| Peaking | 250 Hz   | 1.41 | -2.9 dB |
| Peaking | 500 Hz   | 1.41 | 2.3 dB  |
| Peaking | 1000 Hz  | 1.41 | -2.5 dB |
| Peaking | 2000 Hz  | 1.41 | -1.5 dB |
| Peaking | 4000 Hz  | 1.41 | 3.3 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.0 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Blue%20MOFI%20Active%20On/Blue%20MOFI%20Active%20On.png)