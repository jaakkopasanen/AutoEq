# Skullcandy Aviators no Lens
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 5.9; 31 5.3; 34 4.2; 37 3.2; 41 2.0; 45 1.0; 49 0.1; 54 -0.8; 60 -1.7; 66 -2.4; 72 -3.0; 79 -3.6; 87 -4.0; 96 -4.4; 106 -4.6; 116 -4.7; 128 -4.9; 141 -5.0; 155 -5.0; 170 -4.9; 187 -4.8; 206 -4.8; 227 -4.5; 249 -4.3; 274 -4.0; 302 -3.7; 332 -3.5; 365 -3.3; 402 -3.1; 442 -2.8; 486 -2.7; 535 -2.5; 588 -2.0; 647 -1.7; 712 -1.4; 783 -0.9; 861 -0.7; 947 -0.3; 1042 0.1; 1146 0.8; 1261 1.5; 1387 1.3; 1526 1.8; 1678 2.8; 1846 3.7; 2031 3.9; 2234 3.1; 2457 2.0; 2703 0.3; 2973 -1.3; 3270 -1.9; 3597 -1.1; 3957 -1.5; 4353 -5.3; 4788 -4.7; 5267 -0.6; 5793 2.7; 6373 4.1; 7010 2.4; 7711 0.3; 8482 -0.8; 9330 -2.6; 10263 -2.0; 11289 -0.8; 12418 0.0; 13660 -0.2; 15026 -0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Skullcandy Aviators no Lens GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Skullcandy Aviators no Lens ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.4dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 27 Hz   | 0.73 | 9.1 dB  |
| Peaking | 109 Hz  | 0.25 | -5.8 dB |
| Peaking | 2004 Hz | 1.3  | 5.3 dB  |
| Peaking | 5327 Hz | 0.96 | -9.5 dB |
| Peaking | 6152 Hz | 2.39 | 12.9 dB |
| Peaking | 3130 Hz | 5.01 | -1.5 dB |
| Peaking | 3818 Hz | 4.65 | 3.3 dB  |
| Peaking | 4402 Hz | 5.81 | -3.3 dB |
| Peaking | 9697 Hz | 3.14 | -3.2 dB |
| Peaking | 9812 Hz | 0.99 | 1.6 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Skullcandy%20Aviators%20no%20Lens/Skullcandy%20Aviators%20no%20Lens.png)