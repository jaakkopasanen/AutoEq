# Ultrasone HFI-15G
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -0.8; 66 -2.1; 72 -3.6; 79 -4.7; 87 -5.4; 96 -5.9; 106 -6.5; 116 -7.0; 128 -7.2; 141 -7.2; 155 -6.7; 170 -6.0; 187 -5.4; 206 -5.0; 227 -4.7; 249 -4.3; 274 -3.8; 302 -3.4; 332 -2.9; 365 -2.5; 402 -2.3; 442 -2.2; 486 -1.8; 535 -1.6; 588 -1.6; 647 -1.6; 712 -1.6; 783 -1.8; 861 -2.1; 947 -2.6; 1042 -3.2; 1146 -3.9; 1261 -4.8; 1387 -5.9; 1526 -7.2; 1678 -8.6; 1846 -10.3; 2031 -11.7; 2234 -12.9; 2457 -13.3; 2703 -13.3; 2973 -12.5; 3270 -11.7; 3597 -10.8; 3957 -8.4; 4353 -7.1; 4788 -8.3; 5267 -7.2; 5793 -7.1; 6373 -9.7; 7010 -10.7; 7711 -10.1; 8482 -9.4; 9330 -10.6; 10263 -13.8; 11289 -15.5; 12418 -12.0; 13660 -6.6; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Ultrasone HFI-15G GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Ultrasone HFI-15G ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.3dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 34 Hz    | 0.89 | 7.1 dB  |
| Peaking | 669 Hz   | 0.64 | 5.6 dB  |
| Peaking | 2445 Hz  | 1.39 | -8.3 dB |
| Peaking | 7139 Hz  | 4.41 | -3.2 dB |
| Peaking | 11064 Hz | 2.84 | -9.5 dB |
| Peaking | 60 Hz    | 4.18 | 2.6 dB  |
| Peaking | 123 Hz   | 2.16 | -2.2 dB |
| Peaking | 3582 Hz  | 4.44 | -2.2 dB |
| Peaking | 4080 Hz  | 3.66 | 2.2 dB  |
| Peaking | 13945 Hz | 5.5  | 1.9 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.7 dB  |
| Peaking | 62 Hz    | 1.41 | 4.0 dB  |
| Peaking | 125 Hz   | 1.41 | -2.4 dB |
| Peaking | 250 Hz   | 1.41 | 1.9 dB  |
| Peaking | 500 Hz   | 1.41 | 4.3 dB  |
| Peaking | 1000 Hz  | 1.41 | 5.0 dB  |
| Peaking | 2000 Hz  | 1.41 | -6.9 dB |
| Peaking | 4000 Hz  | 1.41 | -1.0 dB |
| Peaking | 8000 Hz  | 1.41 | -4.8 dB |
| Peaking | 16000 Hz | 1.41 | -0.9 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Ultrasone%20HFI-15G/Ultrasone%20HFI-15G.png)