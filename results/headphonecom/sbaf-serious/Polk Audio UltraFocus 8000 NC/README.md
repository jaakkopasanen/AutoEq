# Polk Audio UltraFocus 8000 NC
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 -5.8; 23 -5.5; 25 -5.3; 28 -5.0; 31 -4.7; 34 -4.5; 37 -4.3; 41 -4.1; 45 -3.8; 49 -3.6; 54 -3.4; 60 -3.0; 66 -2.6; 72 -2.4; 79 -2.4; 87 -2.5; 96 -2.5; 106 -2.3; 116 -2.1; 128 -2.1; 141 -1.9; 155 -1.8; 170 -1.4; 187 -1.6; 206 -1.7; 227 -1.3; 249 -1.0; 274 -0.9; 302 -1.4; 332 -1.3; 365 -0.7; 402 -1.3; 442 -1.4; 486 -1.6; 535 -1.3; 588 -1.0; 647 -1.2; 712 -0.9; 783 -0.3; 861 -0.4; 947 0.0; 1042 0.0; 1146 0.6; 1261 1.5; 1387 1.1; 1526 0.7; 1678 0.3; 1846 0.1; 2031 -0.2; 2234 0.3; 2457 1.5; 2703 2.9; 2973 3.9; 3270 5.0; 3597 6.0; 3957 4.9; 4353 3.8; 4788 -0.2; 5267 1.6; 5793 1.9; 6373 4.5; 7010 2.5; 7711 0.3; 8482 -0.1; 9330 -1.3; 10263 -0.1; 11289 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Polk Audio UltraFocus 8000 NC GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Polk Audio UltraFocus 8000 NC ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.3dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 13 Hz   | 0.71 | -5.2 dB |
| Peaking | 31 Hz   | 0.58 | -2.1 dB |
| Peaking | 130 Hz  | 0.24 | -1.5 dB |
| Peaking | 3500 Hz | 2.49 | 6.1 dB  |
| Peaking | 6461 Hz | 6.63 | 4.4 dB  |
| Peaking | 537 Hz  | 2.57 | -0.6 dB |
| Peaking | 1127 Hz | 4.01 | -0.7 dB |
| Peaking | 1242 Hz | 3.34 | 2.0 dB  |
| Peaking | 2044 Hz | 6.08 | -1.0 dB |
| Peaking | 9371 Hz | 5.76 | -1.6 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Polk%20Audio%20UltraFocus%208000%20NC/Polk%20Audio%20UltraFocus%208000%20NC.png)