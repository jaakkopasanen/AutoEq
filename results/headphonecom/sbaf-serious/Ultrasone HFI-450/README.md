# Ultrasone HFI-450
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 6.0; 41 6.0; 45 6.0; 49 6.0; 54 5.4; 60 3.9; 66 2.7; 72 2.5; 79 3.1; 87 1.9; 96 0.4; 106 -0.4; 116 -0.6; 128 0.2; 141 0.1; 155 0.1; 170 1.1; 187 1.1; 206 1.3; 227 1.3; 249 0.8; 274 -0.6; 302 -1.6; 332 -2.3; 365 -1.9; 402 -1.4; 442 -1.9; 486 -1.1; 535 -0.6; 588 -0.4; 647 -0.2; 712 -0.2; 783 -0.0; 861 0.1; 947 -0.1; 1042 0.1; 1146 0.1; 1261 0.0; 1387 0.0; 1526 0.2; 1678 -0.2; 1846 -2.2; 2031 -1.9; 2234 -1.0; 2457 0.3; 2703 2.1; 2973 2.7; 3270 2.2; 3597 1.7; 3957 6.0; 4353 6.0; 4788 5.8; 5267 2.0; 5793 3.8; 6373 5.5; 7010 1.7; 7711 0.3; 8482 -0.4; 9330 -3.1; 10263 -2.3; 11289 -0.2; 12418 -1.1; 13660 -0.9; 15026 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Ultrasone HFI-450 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Ultrasone HFI-450 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 33 Hz   | 0.79 | 6.9 dB  |
| Peaking | 2888 Hz | 4.02 | 4.0 dB  |
| Peaking | 4346 Hz | 2.32 | 10.6 dB |
| Peaking | 4794 Hz | 0.56 | -4.8 dB |
| Peaking | 6322 Hz | 4.1  | 7.4 dB  |
| Peaking | 111 Hz  | 4.36 | -1.8 dB |
| Peaking | 230 Hz  | 2.16 | 2.3 dB  |
| Peaking | 329 Hz  | 1.61 | -2.9 dB |
| Peaking | 1608 Hz | 1.46 | 1.7 dB  |
| Peaking | 1916 Hz | 4    | -2.7 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Ultrasone%20HFI-450/Ultrasone%20HFI-450.png)