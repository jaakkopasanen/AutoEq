# Beats Solo3 Wired
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -2.8dB
GraphicEQ: 21 -5.8; 23 -6.0; 25 -6.1; 28 -6.2; 31 -6.2; 34 -6.3; 37 -6.4; 41 -6.4; 45 -6.4; 49 -6.5; 54 -6.5; 60 -6.6; 66 -6.8; 72 -6.9; 79 -7.1; 87 -7.2; 96 -7.5; 106 -7.9; 116 -7.8; 128 -7.9; 141 -8.0; 155 -8.1; 170 -7.8; 187 -8.0; 206 -7.7; 227 -7.2; 249 -6.8; 274 -6.1; 302 -5.3; 332 -4.5; 365 -3.8; 402 -2.7; 442 -2.1; 486 -2.0; 535 -1.5; 588 -0.6; 647 -0.0; 712 0.3; 783 0.7; 861 0.4; 947 0.2; 1042 -0.1; 1146 -0.3; 1261 -0.6; 1387 -1.2; 1526 -1.5; 1678 -1.8; 1846 -1.5; 2031 -1.0; 2234 -0.9; 2457 -0.7; 2703 -1.2; 2973 -1.7; 3270 -2.4; 3597 -2.5; 3957 -0.3; 4353 -1.8; 4788 -2.1; 5267 0.8; 5793 2.7; 6373 1.5; 7010 1.7; 7711 0.3; 8482 0.0; 9330 0.0; 10263 0.0; 11289 0.0; 12418 0.0; 13660 0.0; 15026 0.0; 16529 0.0; 18182 -0.6; 20000 -1.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Beats Solo3 Wired GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-27**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beats Solo3 Wired ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-2.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-2.6dB**.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 32 Hz   |  0.29 | -5.9 dB |
| Peaking | 136 Hz  |  0.86 | -4.5 dB |
| Peaking | 246 Hz  |  1.34 | -3.9 dB |
| Peaking | 4012 Hz |  0.85 | -2.5 dB |
| Peaking | 5949 Hz |  2.73 | 4.1 dB  |
| Peaking | 785 Hz  |  2.68 | 1.5 dB  |
| Peaking | 1629 Hz |  3.23 | -1.2 dB |
| Peaking | 2468 Hz |  6.34 | 0.7 dB  |
| Peaking | 4078 Hz | 11.78 | 2.1 dB  |
| Peaking | 4658 Hz |  8.7  | -1.8 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Beats%20Solo3%20Wired/Beats%20Solo3%20Wired.png)