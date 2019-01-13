# Audeze Sine (Cipher Cable)
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -5.0dB
GraphicEQ: 21 0.0; 23 2.6; 25 2.7; 28 2.7; 31 2.6; 34 2.6; 37 2.8; 41 2.7; 45 2.4; 49 2.1; 54 2.0; 60 1.7; 66 1.3; 72 0.9; 79 0.7; 87 0.6; 96 0.0; 106 -0.2; 116 -0.4; 128 -0.5; 141 -0.4; 155 -0.4; 170 -0.2; 187 0.1; 206 0.9; 227 0.7; 249 0.4; 274 0.2; 302 0.2; 332 0.2; 365 0.3; 402 0.3; 442 0.1; 486 -0.1; 535 -0.0; 588 0.0; 647 0.3; 712 0.4; 783 0.4; 861 0.4; 947 0.1; 1042 -0.0; 1146 -0.4; 1261 -0.9; 1387 -1.3; 1526 -1.1; 1678 -1.0; 1846 -1.4; 2031 -1.9; 2234 -2.1; 2457 -1.6; 2703 -2.2; 2973 -2.6; 3270 -2.8; 3597 -2.6; 3957 -0.6; 4353 2.0; 4788 3.4; 5267 3.2; 5793 3.8; 6373 4.8; 7010 2.5; 7711 0.3; 8482 0.0; 9330 0.0; 10263 -1.6; 11289 -4.0; 12418 -3.8; 13660 -2.4; 15026 -1.4; 16529 -4.0; 18182 -7.1; 20000 -6.7
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audeze Sine (Cipher Cable) GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-49**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audeze Sine (Cipher Cable) ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.2dB**.

| Type    | Fc       |     Q | Gain    |
|:--------|:---------|:------|:--------|
| Peaking | 32 Hz    |  0.88 | 3.0 dB  |
| Peaking | 3549 Hz  |  1    | -6.1 dB |
| Peaking | 5099 Hz  |  1.2  | 7.8 dB  |
| Peaking | 11640 Hz |  2.85 | -4.2 dB |
| Peaking | 18922 Hz |  1.23 | -8.0 dB |
| Peaking | 134 Hz   |  2    | -0.9 dB |
| Peaking | 218 Hz   |  4    | 1.0 dB  |
| Peaking | 777 Hz   |  3.09 | 0.7 dB  |
| Peaking | 6566 Hz  | 10.55 | 2.4 dB  |
| Peaking | 7660 Hz  |  5.66 | -1.4 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/usound/Audeze%20Sine%20(Cipher%20Cable)/Audeze%20Sine%20(Cipher%20Cable).png)