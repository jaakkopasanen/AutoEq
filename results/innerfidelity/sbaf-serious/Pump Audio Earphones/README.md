# Pump Audio Earphones

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -4.3dB
GraphicEQ: 21 -13.9; 23 -14.0; 25 -14.0; 28 -13.9; 31 -13.8; 34 -13.8; 37 -13.7; 41 -13.6; 45 -13.5; 49 -13.4; 54 -13.4; 60 -13.3; 66 -13.2; 72 -13.1; 79 -13.1; 87 -13.0; 96 -12.9; 106 -12.6; 116 -12.3; 128 -12.1; 141 -11.8; 155 -11.3; 170 -10.9; 187 -10.3; 206 -9.8; 227 -9.1; 249 -8.5; 274 -7.8; 302 -7.1; 332 -6.5; 365 -5.7; 402 -5.0; 442 -4.1; 486 -3.5; 535 -2.8; 588 -1.5; 647 -0.9; 712 -0.5; 783 0.1; 861 0.2; 947 0.1; 1042 0.0; 1146 -0.0; 1261 -0.1; 1387 -0.6; 1526 -1.1; 1678 -1.9; 1846 -2.8; 2031 -2.8; 2234 -3.2; 2457 -2.3; 2703 -1.6; 2973 0.3; 3270 2.0; 3597 2.4; 3957 1.0; 4353 -2.7; 4788 -7.2; 5267 -9.0; 5793 -1.3; 6373 3.5; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Pump Audio Earphones GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-42**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Pump Audio Earphones ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-1.3dB**.

| Type    | Fc      |     Q | Gain     |
|:--------|:--------|:------|:---------|
| Peaking | 20 Hz   |  0.31 | -12.2 dB |
| Peaking | 140 Hz  |  0.36 | -9.6 dB  |
| Peaking | 2076 Hz |  1.15 | -9.7 dB  |
| Peaking | 2327 Hz |  0.4  | 6.9 dB   |
| Peaking | 5025 Hz |  5.16 | -13.5 dB |
| Peaking | 2721 Hz |  7.43 | -1.1 dB  |
| Peaking | 3475 Hz |  5.32 | 2.0 dB   |
| Peaking | 5490 Hz | 12.04 | -2.4 dB  |
| Peaking | 6507 Hz |  4    | 5.7 dB   |
| Peaking | 7345 Hz |  1.11 | -2.4 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Pump%20Audio%20Earphones/Pump%20Audio%20Earphones.png)