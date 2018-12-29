# Koss KSC75
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 5.5; 41 4.3; 45 3.1; 49 2.1; 54 0.9; 60 -0.4; 66 -1.3; 72 -2.1; 79 -2.9; 87 -3.3; 96 -3.6; 106 -4.2; 116 -4.5; 128 -4.6; 141 -4.7; 155 -4.7; 170 -4.7; 187 -4.6; 206 -4.4; 227 -4.1; 249 -3.7; 274 -3.2; 302 -2.8; 332 -2.4; 365 -2.0; 402 -1.7; 442 -1.4; 486 -1.0; 535 -0.7; 588 -0.4; 647 -0.2; 712 0.0; 783 0.2; 861 0.1; 947 0.1; 1042 -0.0; 1146 -0.2; 1261 -0.5; 1387 -1.1; 1526 -2.1; 1678 -2.8; 1846 -3.5; 2031 -4.1; 2234 -4.2; 2457 -3.4; 2703 -1.6; 2973 0.8; 3270 1.8; 3597 0.9; 3957 4.8; 4353 4.6; 4788 -6.2; 5267 -1.0; 5793 1.6; 6373 2.2; 7010 0.8; 7711 0.3; 8482 -1.0; 9330 -4.8; 10263 -5.6; 11289 -0.2; 12418 0.0; 13660 0.0; 15026 0.0; 16529 0.0; 18182 0.0; 20000 -0.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Koss KSC75 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Koss KSC75 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc      |     Q | Gain     |
|:--------|:--------|:------|:---------|
| Peaking | 30 Hz   |  0.77 | 7.6 dB   |
| Peaking | 127 Hz  |  0.53 | -5.6 dB  |
| Peaking | 2065 Hz |  2.71 | -4.7 dB  |
| Peaking | 4083 Hz | 10.17 | 7.2 dB   |
| Peaking | 9823 Hz |  5.97 | -6.9 dB  |
| Peaking | 773 Hz  |  2.16 | 0.9 dB   |
| Peaking | 2505 Hz |  4.97 | -1.5 dB  |
| Peaking | 3159 Hz |  4.95 | 2.3 dB   |
| Peaking | 4924 Hz |  9.02 | -10.3 dB |
| Peaking | 5596 Hz |  2.1  | 3.1 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Koss%20KSC75/Koss%20KSC75.png)