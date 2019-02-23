# Sennheiser PXC 550 Wired Power On
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -6.2; 23 -6.7; 25 -7.1; 28 -7.5; 31 -7.8; 34 -8.0; 37 -8.2; 41 -8.4; 45 -8.6; 49 -8.8; 54 -8.9; 60 -9.0; 66 -9.0; 72 -9.0; 79 -8.7; 87 -8.8; 96 -8.9; 106 -9.2; 116 -9.7; 128 -10.2; 141 -10.4; 155 -10.5; 170 -8.5; 187 -9.2; 206 -8.4; 227 -7.0; 249 -5.9; 274 -4.9; 302 -4.3; 332 -4.0; 365 -3.9; 402 -4.0; 442 -3.9; 486 -4.2; 535 -4.3; 588 -4.2; 647 -4.4; 712 -4.9; 783 -5.2; 861 -6.0; 947 -6.4; 1042 -6.9; 1146 -6.7; 1261 -6.6; 1387 -7.8; 1526 -8.8; 1678 -9.3; 1846 -8.4; 2031 -8.4; 2234 -7.7; 2457 -6.5; 2703 -5.4; 2973 -4.5; 3270 -3.5; 3597 -3.9; 3957 -3.3; 4353 -0.5; 4788 -9.0; 5267 -7.4; 5793 -2.1; 6373 -1.5; 7010 -3.9; 7711 -6.0; 8482 -9.5; 9330 -12.1; 10263 -8.3; 11289 -6.3; 12418 -6.3; 13660 -6.3; 15026 -6.3; 16529 -6.3; 18182 -6.3; 20000 -8.2
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser PXC 550 Wired Power On GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser PXC 550 Wired Power On ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.0dB**.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 107 Hz  |  1    | -3.8 dB |
| Peaking | 1738 Hz |  2.85 | -3.3 dB |
| Peaking | 3722 Hz |  2.59 | 3.5 dB  |
| Peaking | 6268 Hz |  6.09 | 5.8 dB  |
| Peaking | 9207 Hz |  5    | -6.6 dB |
| Peaking | 46 Hz   |  1.04 | -1.7 dB |
| Peaking | 97 Hz   |  1.83 | 2.6 dB  |
| Peaking | 167 Hz  |  0.91 | -3.3 dB |
| Peaking | 336 Hz  |  0.83 | 4.0 dB  |
| Peaking | 4958 Hz | 12.95 | -5.7 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -1.3 dB |
| Peaking | 62 Hz    | 1.41 | -1.6 dB |
| Peaking | 125 Hz   | 1.41 | -4.2 dB |
| Peaking | 250 Hz   | 1.41 | 0.6 dB  |
| Peaking | 500 Hz   | 1.41 | 3.1 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.4 dB |
| Peaking | 2000 Hz  | 1.41 | -2.9 dB |
| Peaking | 4000 Hz  | 1.41 | 4.2 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.6 dB |
| Peaking | 16000 Hz | 1.41 | -0.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sennheiser%20PXC%20550%20Wired%20Power%20On/Sennheiser%20PXC%20550%20Wired%20Power%20On.png)