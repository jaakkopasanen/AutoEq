# A Audio Elite Bass Mode
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -9.8; 23 -9.3; 25 -8.9; 28 -8.4; 31 -8.0; 34 -7.7; 37 -7.5; 41 -7.3; 45 -7.1; 49 -7.1; 54 -7.0; 60 -6.9; 66 -6.9; 72 -7.0; 79 -7.2; 87 -7.5; 96 -7.9; 106 -8.3; 116 -8.5; 128 -8.6; 141 -9.1; 155 -9.1; 170 -9.2; 187 -9.3; 206 -9.3; 227 -9.1; 249 -8.9; 274 -8.2; 302 -8.2; 332 -8.0; 365 -7.7; 402 -8.1; 442 -8.8; 486 -9.0; 535 -9.7; 588 -10.2; 647 -10.7; 712 -10.4; 783 -10.3; 861 -11.7; 947 -12.2; 1042 -13.2; 1146 -12.5; 1261 -10.7; 1387 -9.4; 1526 -8.3; 1678 -7.2; 1846 -5.7; 2031 -4.2; 2234 -2.9; 2457 -1.6; 2703 -0.7; 2973 -0.6; 3270 -1.4; 3597 -2.1; 3957 -3.7; 4353 -5.7; 4788 -4.9; 5267 -1.2; 5793 -0.5; 6373 -1.0; 7010 -3.9; 7711 -6.2; 8482 -6.4; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`A Audio Elite Bass Mode GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `A Audio Elite Bass Mode ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 21 Hz   | 1.9  | -3.3 dB |
| Peaking | 827 Hz  | 0.1  | -2.4 dB |
| Peaking | 1047 Hz | 1.83 | -5.0 dB |
| Peaking | 2748 Hz | 1.36 | 8.4 dB  |
| Peaking | 5945 Hz | 3.22 | 7.1 dB  |
| Peaking | 178 Hz  | 1.88 | -0.9 dB |
| Peaking | 352 Hz  | 2.3  | 1.3 dB  |
| Peaking | 616 Hz  | 5.49 | -1.2 dB |
| Peaking | 4438 Hz | 2.52 | 2.1 dB  |
| Peaking | 4451 Hz | 5.72 | -4.1 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -2.1 dB |
| Peaking | 62 Hz    | 1.41 | 0.6 dB  |
| Peaking | 125 Hz   | 1.41 | -2.3 dB |
| Peaking | 250 Hz   | 1.41 | -1.6 dB |
| Peaking | 500 Hz   | 1.41 | -1.0 dB |
| Peaking | 1000 Hz  | 1.41 | -7.4 dB |
| Peaking | 2000 Hz  | 1.41 | 3.4 dB  |
| Peaking | 4000 Hz  | 1.41 | 4.3 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.0 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/A%20Audio%20Elite%20Bass%20Mode/A%20Audio%20Elite%20Bass%20Mode.png)