# Phonon SMB2
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.5dB
GraphicEQ: 21 0.0; 23 5.0; 25 4.2; 28 3.1; 31 2.3; 34 1.5; 37 0.9; 41 0.3; 45 -0.2; 49 -0.5; 54 -0.8; 60 -1.1; 66 -1.3; 72 -1.4; 79 -1.5; 87 -1.6; 96 -1.7; 106 -1.8; 116 -1.6; 128 -1.7; 141 -2.0; 155 -2.1; 170 -1.8; 187 -1.8; 206 -1.8; 227 -1.7; 249 -2.0; 274 -1.8; 302 -1.4; 332 -1.0; 365 -0.3; 402 0.5; 442 1.4; 486 1.6; 535 2.0; 588 2.6; 647 2.3; 712 1.6; 783 1.3; 861 0.7; 947 0.2; 1042 -0.0; 1146 -0.1; 1261 -0.1; 1387 -1.0; 1526 -1.8; 1678 -2.4; 1846 -2.3; 2031 -1.4; 2234 0.0; 2457 2.3; 2703 3.6; 2973 5.5; 3270 6.0; 3597 4.9; 3957 5.9; 4353 6.0; 4788 6.0; 5267 6.0; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Phonon SMB2 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-65**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Phonon SMB2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 19 Hz   | 1.16 | 6.7 dB  |
| Peaking | 199 Hz  | 0.21 | -2.3 dB |
| Peaking | 569 Hz  | 1.31 | 4.2 dB  |
| Peaking | 1805 Hz | 2.31 | -4.3 dB |
| Peaking | 4010 Hz | 0.93 | 6.9 dB  |
| Peaking | 2205 Hz | 7.5  | -0.8 dB |
| Peaking | 3207 Hz | 2.71 | 1.9 dB  |
| Peaking | 3684 Hz | 4.77 | -2.6 dB |
| Peaking | 6276 Hz | 2.81 | 4.9 dB  |
| Peaking | 7367 Hz | 1.48 | -3.6 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Phonon%20SMB2/Phonon%20SMB2.png)