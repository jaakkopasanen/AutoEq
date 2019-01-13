# Audeze Sine (Cipher Cable)
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -5.8dB
GraphicEQ: 21 0.0; 23 2.3; 25 2.4; 28 2.3; 31 2.2; 34 2.3; 37 2.4; 41 2.4; 45 2.0; 49 1.8; 54 1.7; 60 1.4; 66 0.9; 72 0.5; 79 0.4; 87 0.3; 96 -0.3; 106 -0.5; 116 -0.7; 128 -0.8; 141 -0.7; 155 -0.8; 170 -0.5; 187 -0.2; 206 0.6; 227 0.4; 249 0.0; 274 -0.2; 302 -0.0; 332 0.1; 365 0.2; 402 0.3; 442 0.1; 486 -0.1; 535 0.1; 588 0.2; 647 0.4; 712 0.6; 783 0.5; 861 0.5; 947 0.2; 1042 -0.0; 1146 -0.4; 1261 -0.5; 1387 -0.7; 1526 -0.2; 1678 -0.0; 1846 -0.4; 2031 -0.6; 2234 -0.2; 2457 0.9; 2703 0.7; 2973 0.5; 3270 0.3; 3597 0.2; 3957 1.8; 4353 4.0; 4788 5.0; 5267 4.9; 5793 5.7; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0; 9330 0.0; 10263 -3.0; 11289 -4.5; 12418 -5.5; 13660 -10.4; 15026 -16.9; 16529 -22.0; 18182 -22.7; 20000 -17.7
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audeze Sine (Cipher Cable) GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-58**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audeze Sine (Cipher Cable) ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.1dB**.

| Type    | Fc       |     Q | Gain     |
|:--------|:---------|:------|:---------|
| Peaking | 31 Hz    |  0.57 | 2.5 dB   |
| Peaking | 121 Hz   |  1.72 | -1.3 dB  |
| Peaking | 5775 Hz  |  1.07 | 11.3 dB  |
| Peaking | 11583 Hz |  0.87 | 9.9 dB   |
| Peaking | 17145 Hz |  0.4  | -27.1 dB |
| Peaking | 214 Hz   |  8    | 0.8 dB   |
| Peaking | 750 Hz   |  2.73 | 0.7 dB   |
| Peaking | 2596 Hz  |  3.65 | 2.6 dB   |
| Peaking | 2717 Hz  |  1.77 | -1.7 dB  |
| Peaking | 7507 Hz  | 10.23 | -1.5 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_in-ear_2017-1/Audeze%20Sine%20(Cipher%20Cable)/Audeze%20Sine%20(Cipher%20Cable).png)