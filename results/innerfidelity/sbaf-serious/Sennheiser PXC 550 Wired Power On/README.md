# Sennheiser PXC 550 Wired Power On
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -5.7; 23 -6.3; 25 -6.7; 28 -7.1; 31 -7.4; 34 -7.6; 37 -7.8; 41 -8.0; 45 -8.2; 49 -8.4; 54 -8.5; 60 -8.5; 66 -8.6; 72 -8.5; 79 -8.3; 87 -8.4; 96 -8.5; 106 -8.8; 116 -9.3; 128 -9.8; 141 -9.9; 155 -10.1; 170 -8.1; 187 -8.8; 206 -8.0; 227 -6.5; 249 -5.4; 274 -4.4; 302 -3.9; 332 -3.6; 365 -3.5; 402 -3.6; 442 -3.5; 486 -3.8; 535 -3.9; 588 -3.8; 647 -4.0; 712 -4.5; 783 -4.8; 861 -5.6; 947 -6.0; 1042 -6.4; 1146 -6.3; 1261 -6.2; 1387 -7.4; 1526 -8.3; 1678 -8.9; 1846 -8.0; 2031 -8.0; 2234 -7.3; 2457 -6.1; 2703 -4.9; 2973 -4.1; 3270 -3.1; 3597 -3.5; 3957 -2.9; 4353 -0.5; 4788 -8.5; 5267 -7.0; 5793 -1.7; 6373 -1.1; 7010 -3.8; 7711 -6.0; 8482 -9.1; 9330 -11.7; 10263 -7.9; 11289 -6.3; 12418 -6.3; 13660 -6.3; 15026 -6.3; 16529 -6.3; 18182 -6.3; 20000 -7.7
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser PXC 550 Wired Power On GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser PXC 550 Wired Power On ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.3dB**.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 488 Hz  |  0.46 | 10.4 dB |
| Peaking | 523 Hz  |  0.13 | -7.3 dB |
| Peaking | 3449 Hz |  1.53 | 6.7 dB  |
| Peaking | 6301 Hz |  5.13 | 6.8 dB  |
| Peaking | 9251 Hz |  5.6  | -5.8 dB |
| Peaking | 15 Hz   |  1.72 | 2.6 dB  |
| Peaking | 148 Hz  |  4.65 | -1.7 dB |
| Peaking | 290 Hz  |  4.44 | 1.4 dB  |
| Peaking | 4321 Hz | 10.81 | 5.1 dB  |
| Peaking | 4930 Hz |  9.93 | -5.5 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -0.8 dB |
| Peaking | 62 Hz    | 1.41 | -1.3 dB |
| Peaking | 125 Hz   | 1.41 | -3.8 dB |
| Peaking | 250 Hz   | 1.41 | 0.9 dB  |
| Peaking | 500 Hz   | 1.41 | 3.4 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.1 dB |
| Peaking | 2000 Hz  | 1.41 | -2.5 dB |
| Peaking | 4000 Hz  | 1.41 | 4.5 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.3 dB |
| Peaking | 16000 Hz | 1.41 | -0.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sennheiser%20PXC%20550%20Wired%20Power%20On/Sennheiser%20PXC%20550%20Wired%20Power%20On.png)