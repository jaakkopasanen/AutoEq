# Klipsch X-10i
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 -1.6; 23 -1.7; 25 -1.8; 28 -1.9; 31 -2.0; 34 -2.0; 37 -2.1; 41 -2.2; 45 -2.3; 49 -2.5; 54 -2.7; 60 -3.0; 66 -3.3; 72 -3.5; 79 -3.6; 87 -3.9; 96 -4.3; 106 -4.3; 116 -4.5; 128 -4.6; 141 -4.9; 155 -4.9; 170 -4.9; 187 -4.9; 206 -4.7; 227 -4.6; 249 -4.4; 274 -4.1; 302 -3.8; 332 -3.4; 365 -2.9; 402 -2.5; 442 -2.2; 486 -1.8; 535 -1.3; 588 -0.8; 647 -0.3; 712 0.0; 783 0.2; 861 0.3; 947 0.1; 1042 -0.2; 1146 -0.5; 1261 -0.9; 1387 -1.4; 1526 -1.9; 1678 -1.9; 1846 -1.6; 2031 -1.4; 2234 -1.2; 2457 -1.2; 2703 -1.4; 2973 -0.8; 3270 2.3; 3597 5.7; 3957 6.0; 4353 6.0; 4788 5.9; 5267 6.0; 5793 6.0; 6373 5.0; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Klipsch X-10i GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Klipsch X-10i ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 52 Hz   | 0.35 | -1.9 dB |
| Peaking | 151 Hz  | 0.75 | -3.4 dB |
| Peaking | 290 Hz  | 1.34 | -2.0 dB |
| Peaking | 2558 Hz | 1.12 | -4.3 dB |
| Peaking | 4322 Hz | 1.25 | 8.5 dB  |
| Peaking | 823 Hz  | 2.83 | 1.0 dB  |
| Peaking | 1525 Hz | 5.05 | -1.1 dB |
| Peaking | 4688 Hz | 5.45 | -2.0 dB |
| Peaking | 6396 Hz | 1.84 | 4.5 dB  |
| Peaking | 7512 Hz | 1.73 | -4.1 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Klipsch%20X-10i/Klipsch%20X-10i.png)